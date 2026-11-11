# Questões de análise

As questões a seguir delimitam a análise descritiva da produção hospitalar e dos leitos cadastrados.

| Pergunta | Como foi respondida | Evidência |
|---|---|---|
| Qual problema será analisado? | Distribuição da produção administrativa e da estrutura cadastrada no recorte DF. | README e metodologia |
| Qual é a unidade de análise? | Estabelecimento identificado por CNES e competência de processamento. | CSV agregado |
| Quais estabelecimentos concentram registros? | Ordenação decrescente de registros RD; gráfico dos dez maiores e participação calculada. | Gráfico 01, indicadores.json |
| Como os valores registrados se distribuem? | Soma de VAL_TOT por estabelecimento, preservada em centavos. | Gráfico 02 |
| Como se distribuem os leitos cadastrados? | Comparação de QT_EXIST e QT_SUS nos estabelecimentos com produção RD. | Gráfico 03 |
| O que a dispersão entre leitos e produção permite observar? | Posição e dispersão dos estabelecimentos em duas medidas; sem atribuição causal ou avaliação de eficiência. | Gráfico 04 |
| Como a qualidade foi avaliada? | Verificações explícitas de chave, formato, ausência, domínio e conservação. | verificacoes.json |
| Qual foi a conclusão? | A análise permite descrever concentração e diferenças no recorte; não comprova desempenho assistencial. | resultados_e_limitacoes.md |
| Como reproduzir? | Instalar dependências e executar o script com o CSV incluído. | README |

Os resultados quantitativos são apresentados no relatório de análise e nos arquivos de indicadores gerados pelo código.
