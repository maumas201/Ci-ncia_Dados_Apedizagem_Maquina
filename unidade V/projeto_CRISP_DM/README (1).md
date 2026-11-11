# Dados, dicionário e procedência

A fonte institucional dos dados é o Ministério da Saúde, por meio do DATASUS. Foram utilizados os arquivos **RDDF2506.dbc** (SIH/SUS — AIH reduzida), **STDF2506.dbc** (CNES — estabelecimentos) e **LTDF2506.dbc** (CNES — leitos), referentes ao Distrito Federal e à competência de junho de 2025.

`integracao_por_estabelecimento.csv` resulta do piloto realizado com esses arquivos, recebidos em 16/10/2026. RD e LT foram agregados separadamente por CNES e competência e associados aos atributos do ST. Esta atividade utiliza o agregado preservado, sem nova aquisição dos microdados. Os hashes dos arquivos originais constam de `reproducao/inventario_originais.json`; o hash da tabela analisada está em `resultados/execucao.json`. A data de recebimento identifica a entrada dos arquivos no estudo, não a data do download no portal de origem.

Grão: CNES + COMPETEN. Universo: estabelecimentos com registros no RDDF2506 e atributos correspondentes do CNES; não é o universo integral do cadastro LT nem exclusivamente hospitais de propriedade pública. Competência de processamento não é sinônimo de mês de início de todas as internações.

| Campo | Uso e interpretação |
|---|---|
| CNES | Código do estabelecimento; texto para preservar zeros |
| COMPETEN | Competência YYYYMM; texto |
| registros_rd | Quantidade de linhas RD, não pessoas únicas |
| aih_normais | Registros com IDENT=1 |
| aih_continuacao | Registros com IDENT=5 |
| valor_total_centavos | Soma de VAL_TOT convertida em centavos |
| QT_EXIST | Leitos existentes cadastrados, agregados do LT |
| QT_SUS | Leitos SUS cadastrados; subconjunto dos existentes |
| QT_NSUS | Leitos não SUS cadastrados |
| dias_permanencia_registrados | Soma histórica de DIAS_PERM; não usada nos gráficos desta atividade |
| obitos_registrados | Soma histórica do indicador de óbito; não usada para comparar qualidade |
| TP_UNID | Código cadastral de tipo de estabelecimento; sem tradução neste estudo |
| NAT_JUR | Código cadastral de natureza jurídica; sem tradução neste estudo |

Campos herdados não empregados na análise são preservados para rastreabilidade; sua presença não significa que tenham sido validados para qualquer uso. A verificação física do leiaute não constitui certificação semântica de todos os campos da versão de 2025.

## Reprodução desde os originais
O script histórico está em `reproducao/analisar_piloto.py`. Para executar essa etapa opcional, coloque RDDF2506.dbc, STDF2506.dbc e LTDF2506.dbc em `reproducao/dados/brutos/` e instale as dependências de `reproducao/requirements.txt`. Execute `python reproducao/analisar_piloto.py`. Ele gera resultados em `reproducao/resultados/`; compare o CSV regenerado com o CSV de entrada da atividade antes de substituí-lo. Os arquivos individuais DBC e DBF não integram o pacote de análise.

A atividade principal começa nos agregados e dispensa os DBC. Os hashes permitem verificar a integridade dos arquivos utilizados.


## Nomes dos estabelecimentos
Os nomes foram consultados nas fichas oficiais do CNES em 11/11/2026 e relacionados pelo código CNES com cardinalidade um para um. A tabela `dados/nomes_estabelecimentos.csv` preserva nome consultado, rótulo, URL e data da consulta. Para siglas isoladas (HRAN, HRG, HRS, HRPL, HRBZ, HRL e HRSM), foi usado o nome empresarial da mesma ficha. A capitalização foi ajustada apenas para leitura. As denominações correspondem à consulta de novembro/2026 e não constituem um cadastro histórico de junho/2025; os dados quantitativos continuam naquela competência. O arquivo ST inspecionado não contém campo de nome. Uma mudança de nome posterior não altera os valores nem autoriza deduzir mudanças de gestão.
