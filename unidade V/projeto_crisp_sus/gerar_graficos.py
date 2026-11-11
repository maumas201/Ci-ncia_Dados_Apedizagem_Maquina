"""Análise descritiva de agregados SIH/CNES. Execute da raiz: python src/gerar_graficos.py."""
from pathlib import Path
import hashlib
import json
import platform
import textwrap
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

ROOT = Path(__file__).resolve().parents[1]

def main():
    entrada = ROOT / 'dados/integracao_por_estabelecimento.csv'
    df = pd.read_csv(entrada, dtype={'CNES': 'string', 'COMPETEN': 'string'})
    nomes = pd.read_csv(ROOT / 'dados/nomes_estabelecimentos.csv', dtype={'CNES':'string'})
    df = df.merge(nomes, on='CNES', how='left', validate='one_to_one')
    if df.nome_exibicao.isna().any():
        raise ValueError('Nome de estabelecimento não localizado')
    df['rotulo'] = df.apply(lambda x: textwrap.fill(x.nome_exibicao, 38) + '\nCNES ' + x.CNES, axis=1)
    ref = json.loads((ROOT/'reproducao/resumo_piloto.json').read_text(encoding='utf-8'))
    verificacoes = {
        'nomes_completos': df.nome_exibicao.notna().all(),
        'chave_unica': not df.duplicated(['CNES','COMPETEN']).any(),
        'competencia': df.COMPETEN.eq('202506').all(),
        'cnes_formato': df.CNES.str.fullmatch(r'\d{7}').all(),
        'ausencias_campos_usados': not df[['CNES','COMPETEN','registros_rd','aih_normais','aih_continuacao','valor_total_centavos','QT_EXIST','QT_SUS']].isna().any().any(),
        'contagem_preservada': int(df.registros_rd.sum()) == ref['inventario'][0]['linhas'],
        'tipos_preservados': (df.registros_rd == df.aih_normais + df.aih_continuacao).all(),
        'valor_preservado': int(df.valor_total_centavos.sum()) == ref['valor_total_centavos'],
        'leitos_subuniverso': int(df.QT_SUS.sum()) == ref['leitos_apenas_cnes_com_rd']['QT_SUS'],
        'nao_negativos': df[['registros_rd','valor_total_centavos','QT_EXIST','QT_SUS']].ge(0).all().all(),
        'leitos_sus_limite': df.QT_SUS.le(df.QT_EXIST).all(),
    }
    verificacoes = {k: bool(v) for k,v in verificacoes.items()}
    (ROOT/'resultados').mkdir(exist_ok=True)
    (ROOT/'graficos').mkdir(exist_ok=True)
    (ROOT/'resultados/verificacoes.json').write_text(json.dumps(verificacoes,indent=2),encoding='utf-8')
    if not all(verificacoes.values()):
        raise ValueError('Falha na verificação: consulte resultados/verificacoes.json')
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False})
    fmt = FuncFormatter(lambda x,pos: f'{x:,.0f}'.replace(',','.'))
    fonte = 'Fonte: SIH/SUS RD e CNES LT; agregados do piloto. Competência de processamento: jun/2025.'
    def salvar(fig, nome):
        fig.text(.02,.04,fonte,fontsize=8,color='#475569')
        fig.text(.02,.015,'Nomes: fichas CNES consultadas em 11/11/2026; denominações históricas de jun/2025 não confirmadas.',fontsize=8,color='#475569')
        fig.savefig(ROOT/'graficos'/nome,dpi=160,bbox_inches='tight')
        plt.close(fig)
    top = df.sort_values(['registros_rd','CNES'],ascending=[False,True]).head(10).sort_values('registros_rd')
    fig,ax=plt.subplots(figsize=(14,9)); fig.subplots_adjust(left=.34,bottom=.15,top=.85)
    ax.barh(top.rotulo,top.registros_rd,color='#146b8c')
    ax.bar_label(ax.containers[0],padding=4,labels=[f'{n:,}'.replace(',','.') for n in top.registros_rd])
    ax.set_xlim(0,top.registros_rd.max()*1.15);ax.xaxis.set_major_formatter(fmt)
    ax.set(xlabel='Registros de AIH (normais + prorrogações)',ylabel='')
    fig.suptitle('Produção registrada: dez maiores volumes no recorte',fontsize=16,fontweight='bold')
    ax.set_title('DF • Ordenação por volume, sem avaliação de qualidade hospitalar',fontsize=10)
    salvar(fig,'01_registros_por_estabelecimento.png')
    topv=df.sort_values(['valor_total_centavos','CNES'],ascending=[False,True]).head(10).sort_values('valor_total_centavos')
    fig,ax=plt.subplots(figsize=(14,9));fig.subplots_adjust(left=.34,bottom=.15,top=.85)
    ax.barh(topv.rotulo,topv.valor_total_centavos/100_000_000,color='#477955')
    ax.set(xlabel='Soma de VAL_TOT (R$ milhões)',ylabel='')
    fig.suptitle('Valor total registrado: dez maiores somas',fontsize=16,fontweight='bold')
    ax.set_title('Não representa custo econômico nem comprovação de desembolso',fontsize=10)
    salvar(fig,'02_valor_por_estabelecimento.png')
    topb=df.sort_values(['QT_SUS','CNES'],ascending=[False,True]).head(10).sort_values('QT_SUS')
    fig,ax=plt.subplots(figsize=(14,9));fig.subplots_adjust(left=.34,bottom=.15,top=.85)
    ax.barh(topb.rotulo,topb.QT_EXIST,color='#d2dbe4',label='Existentes (incluem SUS)')
    ax.barh(topb.rotulo,topb.QT_SUS,color='#835ba5',label='SUS')
    ax.set(xlabel='Leitos cadastrados',ylabel='');ax.legend(loc='lower right')
    fig.suptitle('Leitos cadastrados nos estabelecimentos com produção RD',fontsize=15,fontweight='bold')
    ax.set_title('Dez maiores QT_SUS do recorte • Estoque cadastral, não disponibilidade diária',fontsize=10)
    salvar(fig,'03_leitos_cadastrados.png')
    fig,ax=plt.subplots(figsize=(9,6.5));fig.subplots_adjust(left=.13,bottom=.17,top=.84)
    ax.scatter(df.QT_SUS,df.registros_rd,s=55,c='#146b8c',alpha=.8,edgecolor='white')
    ax.set(xlabel='Leitos SUS cadastrados',ylabel='Registros de AIH');ax.yaxis.set_major_formatter(fmt)
    fig.suptitle('Produção registrada e estrutura cadastrada',fontsize=16,fontweight='bold')
    ax.set_title('Cada ponto é um estabelecimento • Não mede ocupação, eficiência ou causalidade',fontsize=10)
    salvar(fig,'04_producao_e_leitos.png')
    lider=df.sort_values(['registros_rd','CNES'],ascending=[False,True]).iloc[0]
    r={'estabelecimentos':len(df),'registros_aih':int(df.registros_rd.sum()),'aih_normais':int(df.aih_normais.sum()),'aih_prorrogacao':int(df.aih_continuacao.sum()),'valor_total_centavos':int(df.valor_total_centavos.sum()),'leitos_sus_recorte':int(df.QT_SUS.sum()),'leitos_existentes_recorte':int(df.QT_EXIST.sum()),'maior_volume_cnes':str(lider.CNES),'maior_volume_registros':int(lider.registros_rd),'participacao_dez_maiores_percentual':float(top.registros_rd.sum()/df.registros_rd.sum()*100)}
    (ROOT/'resultados/indicadores.json').write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding='utf-8')
    df.sort_values('registros_rd',ascending=False).to_csv(ROOT/'resultados/tabela_analisada.csv',index=False,encoding='utf-8')
    m={'sha256_nomes':hashlib.sha256((ROOT/'dados/nomes_estabelecimentos.csv').read_bytes()).hexdigest(),'sha256_csv':hashlib.sha256(entrada.read_bytes()).hexdigest(),'python':platform.python_version(),'pandas':pd.__version__,'matplotlib':matplotlib.__version__,'conciliacao_tabnet':'nao_realizada','escopo':'reprodução a partir de agregados, não nova extração DBC'}
    (ROOT/'resultados/execucao.json').write_text(json.dumps(m,indent=2),encoding='utf-8')
    texto=f'''# Resultados da análise\n\nGerado por `src/gerar_graficos.py`.\n\nO recorte inclui {r['estabelecimentos']} estabelecimentos, {r['registros_aih']} registros de AIH, sendo {r['aih_normais']} normais e {r['aih_prorrogacao']} prorrogações. O maior volume é do CNES {r['maior_volume_cnes']}, com {r['maior_volume_registros']} registros. Os dez maiores volumes concentram {r['participacao_dez_maiores_percentual']:.2f}% dos registros do recorte.\n\nA soma de VAL_TOT é R$ {r['valor_total_centavos']/100:.2f}. Os estabelecimentos com produção no RD totalizam {r['leitos_sus_recorte']} leitos SUS cadastrados e {r['leitos_existentes_recorte']} existentes. Esse universo não corresponde a todos os estabelecimentos do LT.\n\n## Interpretação dos gráficos\n\n1. Barras de produção: permitem comparar volume registrado e identificar concentração. O gráfico mostra apenas os dez maiores, mas os totais usam a base completa. Volume não é qualidade.\n2. Barras monetárias: comparam somas administrativas. Diferenças podem refletir volume e composição dos procedimentos; não demonstram eficiência ou custo hospitalar.\n3. Barras de leitos: mostram capacidade cadastrada do subuniverso com produção. Leitos SUS estão contidos nos existentes, por isso as barras não são somadas.\n4. Dispersão: permite explorar a distribuição conjunta de volume e leitos. Não demonstra relação causal e não é taxa de ocupação.\n\n## Limitações\n\nUma competência de processamento não representa exatamente internações iniciadas naquele mês. Registros não representam pessoas únicas. Há diferenças entre especialidades e perfis de atendimento não controladas nesta análise. Os gráficos exibem nomes consultados nas fichas oficiais do CNES em 11/11/2026, mantendo os códigos. Não se confirmou a denominação histórica de junho/2025. Os rótulos não alteram o universo nem os valores. O estudo é descritivo, sem inferência estatística, previsão ou avaliação com usuários. A avaliação de dados se limita à consistência interna, sem conciliação independente com TABNET. Os testes comparam o CSV a evidências do mesmo piloto: consistência interna não é validação externa.\n'''
    (ROOT/'docs/resultados_e_limitacoes.md').write_text(texto,encoding='utf-8')
    print(json.dumps(r,ensure_ascii=False,indent=2))
    return r

if __name__=='__main__':
    main()
