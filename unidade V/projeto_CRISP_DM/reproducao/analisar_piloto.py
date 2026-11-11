"""Piloto SIH/CNES — lê os originais sem alterar ou deduplicar registros.

Execução: python analisar_piloto.py
Dependências e explicações: README.md e GUIA_ESTUDO.md.
Os resultados são exploratórios, não uma base clínica validada.
"""
from pathlib import Path
from decimal import Decimal
import hashlib
import json
import platform
import importlib.metadata
from datetime import datetime, timezone

import pandas as pd
from dbfread import DBF
from pyreaddbc import dbc2dbf

ROOT = Path(__file__).resolve().parent
RAW = ROOT / 'dados' / 'brutos'
WORK = ROOT / 'dados' / 'derivados'
OUT = ROOT / 'resultados'
for folder in (RAW, WORK, OUT):
    folder.mkdir(parents=True, exist_ok=True)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save_json(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2,
                                      default=str), encoding='utf-8')


def save_table(name, frame):
    frame.to_csv(OUT / name, index=False, encoding='utf-8-sig')


def missing(series):
    """Ausência física = None/NaN OU texto vazio; zero não vira ausente."""
    return series.isna() | series.astype('string').str.strip().eq('').fillna(False)


def cents(series):
    """Somar dinheiro em centavos evita erro acumulado de ponto flutuante."""
    return sum(int(Decimal(str(v)) * 100) for v in series)


def read_source(prefix):
    path = RAW / f'{prefix}DF2506.dbc'
    before = sha256(path)
    dest = WORK / f'{prefix}DF2506.dbf'
    dbc2dbf(str(path), str(dest))
    table = DBF(str(dest), encoding='latin1', load=True)
    df = pd.DataFrame(iter(table))
    assert len(df) == table.header.numrecords, 'Contagem difere do cabeçalho DBF'
    assert before == sha256(path), 'Arquivo original foi alterado'
    assert not df.columns.duplicated().any()
    assert not missing(df.CNES).any()
    assert df.CNES.str.fullmatch(r'\d{7}').all()
    profile = []
    for field in table.fields:
        s = df[field.name]
        blank = missing(s)
        numeric = pd.api.types.is_numeric_dtype(s)
        profile.append({
            'fonte': prefix, 'campo': field.name, 'tipo_dbf': field.type,
            'largura': field.length, 'decimais': field.decimal_count,
            'tipo_pandas': str(s.dtype), 'linhas': len(s),
            'nulos_python': int(s.isna().sum()),
            'ausentes_incluindo_brancos': int(blank.sum()),
            'percentual_ausente': round(100 * blank.mean(), 4),
            'distintos_preenchidos': int(s[~blank].nunique()),
            'zeros_numericos': int(s.eq(0).sum()) if numeric else None,
            'strings_so_zeros': int(s.astype('string').str.fullmatch('0+').fillna(False).sum()) if not numeric else None,
            'min_numerico': s.min() if numeric else None,
            'max_numerico': s.max() if numeric else None,
            'obrigatoriedade_oficial': 'Não confirmada para o layout 202506',
            'semantica': 'Consultar DICIONARIO_PRELIMINAR.md; não inferir pelo nome',
        })
    save_table(f'perfil_{prefix}.csv', pd.DataFrame(profile))
    inventory = {'arquivo': path.name, 'bytes_dbc': path.stat().st_size,
                 'sha256': before, 'bytes_dbf': dest.stat().st_size,
                 'sha256_dbf': sha256(dest), 'linhas': len(df),
                 'colunas': len(df.columns), 'cnes_distintos': int(df.CNES.nunique()),
                 'duplicatas_completas': int(df.duplicated().sum()),
                 'nulos_python': int(df.isna().sum().sum()),
                 'ausentes_com_brancos': sum(x['ausentes_incluindo_brancos'] for x in profile),
                 'origem_recebida': 'DATASUS — SIH/SUS RD e CNES ST/LT, DF, competência 202506; arquivos recebidos em 16/10/2026',
                 'download_original_em': None, 'url_original_confirmada': None,
                 'versao_layout': 'Cabeçalho físico inspecionado; correspondência documental integral não verificada'}
    return df, inventory


def main():
    pairs = [read_source(x) for x in ('RD', 'ST', 'LT')]
    rd, st, lt = [x[0] for x in pairs]
    save_json('inventario.json', [x[1] for x in pairs])
    # Competências permanecem distintas conceitualmente, embora iguais no piloto.
    rd['COMPETEN'] = rd.ANO_CMPT + rd.MES_CMPT
    for df in (rd, st, lt):
        assert df.COMPETEN.eq('202506').all()
    assert rd.MUNIC_MOV.eq('530010').all()
    assert st.CODUFMUN.eq('530010').all() and lt.CODUFMUN.eq('530010').all()
    key = ['CNES', 'COMPETEN']
    assert not st.duplicated(key).any()
    assert not lt.duplicated(key + ['CODLEITO']).any()
    assert rd.IDENT.isin(['1', '5']).all()
    assert rd.MORTE.isin([0, 1]).all()
    assert (lt[['QT_EXIST', 'QT_SUS', 'QT_NSUS', 'QT_CONTR']] >= 0).all().all()
    assert (lt.QT_SUS <= lt.QT_EXIST).all()
    assert lt.QT_EXIST.eq(lt.QT_SUS + lt.QT_NSUS).all()

    # Teste deliberado da junção inadequada: apenas chaves, sem dados pessoais.
    wrong = rd[key].merge(lt[key], on=key, how='left')
    enriched = rd.merge(st[key + ['TP_UNID', 'NAT_JUR']], on=key, how='left',
                        validate='many_to_one', indicator=True, suffixes=('', '_ST'))
    assert len(enriched) == len(rd) and enriched['_merge'].eq('both').all()
    assert cents(enriched.VAL_TOT) == cents(rd.VAL_TOT)
    assert enriched.DIAS_PERM.sum() == rd.DIAS_PERM.sum()

    # Uma linha por estabelecimento/competência em cada fato agregado.
    rd['normal'] = rd.IDENT.eq('1').astype(int)
    rd['continuacao'] = rd.IDENT.eq('5').astype(int)
    rd['valor_centavos'] = rd.VAL_TOT.map(lambda v: int(Decimal(str(v)) * 100))
    facts = rd.groupby(key, as_index=False).agg(
        registros_rd=('CNES', 'size'), aih_normais=('normal', 'sum'),
        aih_continuacao=('continuacao', 'sum'),
        dias_permanencia_registrados=('DIAS_PERM', 'sum'),
        obitos_registrados=('MORTE', 'sum'), valor_total_centavos=('valor_centavos', 'sum'))
    beds = lt.groupby(key, as_index=False)[['QT_EXIST', 'QT_SUS', 'QT_NSUS']].sum()
    joined = facts.merge(beds, on=key, how='left', validate='one_to_one', indicator=True)
    assert joined['_merge'].eq('both').all()
    assert len(joined) == rd.CNES.nunique()
    assert joined.registros_rd.sum() == len(rd)
    assert joined.valor_total_centavos.sum() == cents(rd.VAL_TOT)
    joined = joined.drop(columns='_merge').merge(st[key + ['TP_UNID', 'NAT_JUR']],
                                               on=key, validate='one_to_one')
    save_table('integracao_por_estabelecimento.csv', joined)
    save_table('leitos_por_tipo_codigo.csv', lt.groupby(['TP_LEITO', 'CODLEITO'], as_index=False)[['QT_EXIST', 'QT_SUS', 'QT_NSUS']].sum())

    dates = {}
    for col in ['DT_INTER', 'DT_SAIDA']:
        parsed = pd.to_datetime(rd[col], format='%Y%m%d', errors='coerce')
        assert parsed.notna().all()
        dates[col] = {'min': str(parsed.min().date()), 'max': str(parsed.max().date()),
                      'por_mes': parsed.dt.strftime('%Y%m').value_counts().sort_index().to_dict()}
    elapsed = (pd.to_datetime(rd.DT_SAIDA) - pd.to_datetime(rd.DT_INTER)).dt.days
    assert (elapsed >= 0).all()
    difference = elapsed.ne(rd.DIAS_PERM)
    duplicate_groups = []
    for idx, (_, group) in enumerate(rd[rd.duplicated('N_AIH', keep=False)].groupby('N_AIH'), 1):
        duplicate_groups.append({'grupo_local': idx, 'linhas': len(group),
                                 'tipos_aih': group.IDENT.tolist(),
                                 'campos_diferentes': [c for c in group.columns if group[c].nunique() > 1]})
    save_json('aih_repetidas_sem_identificadores.json', duplicate_groups)
    missing_keys = {
        'RD_sem_ST': sorted(set(rd.CNES) - set(st.CNES)),
        'RD_sem_LT': sorted(set(rd.CNES) - set(lt.CNES)),
        'LT_sem_ST': sorted(set(lt.CNES) - set(st.CNES))}
    # O catálogo mantém a média de permanência em revisão devido à divergência observada.
    result = {'inventario': [x[1] for x in pairs], 'datas': dates,
              'tipos_aih': rd.IDENT.value_counts().to_dict(),
              'aih_distintas': int(rd.N_AIH.nunique()),
              'excesso_sobre_aih_distintas': int(rd.duplicated('N_AIH').sum()),
              'linhas_na_juncao_inadequada': len(wrong),
              'fator_multiplicacao': len(wrong) / len(rd),
              'linhas_rd_st': len(enriched), 'linhas_agregadas': len(joined),
              'chaves_sem_correspondencia': missing_keys,
              'leitos_todos_lt': lt[['QT_EXIST', 'QT_SUS', 'QT_NSUS', 'QT_CONTR']].sum().to_dict(),
              'leitos_apenas_cnes_com_rd': joined[['QT_EXIST', 'QT_SUS', 'QT_NSUS']].sum().to_dict(),
              'dias_permanencia': int(rd.DIAS_PERM.sum()),
              'obitos_registrados': int(rd.MORTE.sum()),
              'valor_total_centavos': cents(rd.VAL_TOT),
              'dias_diferentes_intervalo_datas': int(difference.sum()),
              'divergencias_dias_por_ident': rd.loc[difference, 'IDENT'].value_counts().to_dict(),
              'maior_intervalo_datas': int(elapsed.max()),
              'saida_fora_junho': int((~rd.DT_SAIDA.str.startswith('202506')).sum()),
              'naturezas_juridicas_rd': rd.NAT_JUR.value_counts().to_dict(),
              'tipos_estabelecimento_com_rd': st[st.CNES.isin(rd.CNES)].TP_UNID.value_counts().to_dict(),
              'testes_estruturais': 'PASSARAM',
              'reconciliacao_tabnet': 'NAO_REALIZADA',
              'validacao_utilidade_com_profissionais': 'NÃO REALIZADA'}
    save_json('resumo.json', result)
    save_json('execucao.json', {'executado_utc': datetime.now(timezone.utc).isoformat(),
                              'python': platform.python_version(),
                              'pacotes': {p: importlib.metadata.version(p) for p in ['pandas', 'dbfread', 'pyreaddbc']},
                              'sha256_script': sha256(Path(__file__)),
                              'encoding_dbf': 'latin1',
                              'status': 'Concluído com pendências semânticas; ver relatório'})
    print(json.dumps({k:v for k,v in result.items() if k not in ('inventario', 'datas')}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
