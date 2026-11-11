# Fontes e materiais

Consulta em 11/11/2026, exceto quando indicado como registro histórico.

- Material didático da disciplina: *Guia Definitivo: O Modelo CRISP-DM*, arquivo Guia_Prático_CRISP-DM.pdf, 13 páginas. Identifica a disciplina Ciência de Dados e Aprendizagem de Máquina e a docente Profa. Kadidja Valéria. Usado como roteiro didático, não como comprovação de resultados do estudo.
- IBM. CRISP-DM Help Overview. https://www.ibm.com/docs/en/spss-modeler/18.6.0?topic=dm-crisp-help-overview
- IBM. Deployment Overview. https://www.ibm.com/docs/en/spss-modeler/saas?topic=deployment-overview
- DATASUS. Procedimentos Hospitalares do SUS por local de internação — Notas Técnicas. https://tabnet.datasus.gov.br/cgi/sih/Proced_hosp_loc_int_2008.pdf
- Ministério da Saúde / DATASUS. SIH/SUS, arquivo de AIH reduzida **RDDF2506.dbc**, Distrito Federal, processamento de junho de 2025.
- Ministério da Saúde / DATASUS. CNES, arquivos **STDF2506.dbc** (estabelecimentos) e **LTDF2506.dbc** (leitos), Distrito Federal, competência de junho de 2025.
- Procedência no estudo: arquivos originais recebidos em 16/10/2026 e preservados por hash; tabela analítica derivada da agregação e integração por CNES e competência.
- Evidências locais: CSV agregado, resumo e inventário do piloto reproduzido; ver `reproducao/`.


## Nomes dos estabelecimentos
Os nomes foram consultados nas fichas oficiais do CNES em 11/11/2026 e relacionados pelo código CNES com cardinalidade um para um. A tabela `dados/nomes_estabelecimentos.csv` preserva nome consultado, rótulo, URL e data da consulta. Para siglas isoladas (HRAN, HRG, HRS, HRPL, HRBZ, HRL e HRSM), foi usado o nome empresarial da mesma ficha. A capitalização foi ajustada apenas para leitura. As denominações correspondem à consulta de novembro/2026 e não constituem um cadastro histórico de junho/2025; os dados quantitativos continuam naquela competência. O arquivo ST inspecionado não contém campo de nome. Uma mudança de nome posterior não altera os valores nem autoriza deduzir mudanças de gestão.
