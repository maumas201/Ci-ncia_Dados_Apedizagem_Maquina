![UDF Centro Universitário](assets/logo-udf.png)

**Ciência de Dados e Aprendizado de Máquina — UDF — 2026.2**  
**Professora:** Kadidja Valéria  
**Curso:** Sistemas de Informação — noturno, quarta-feira  
**Integrantes:** Maurício Rafael Oliveira da Silva e Gabriel Silva

# Atividades de Machine Learning

Neste projeto, reunimos os exercícios sobre os conceitos de Machine Learning, duas propostas de solução de problemas e um laboratório em Python. Trabalhamos com exemplos didáticos e dados sintéticos para entender como preparar os dados, treinar modelos e interpretar os resultados.

## Atividades

| Arquivo | Conteúdo |
| --- | --- |
| [01 — Conceitos e tipos de aprendizado](01-aula1-conceitos.md) | Conceitos, comparação de abordagens e classificação de situações |
| [02 — PBL Biblioteca](02-pbl-biblioteca.md) | Proposta para analisar atendimento e demanda de uma biblioteca |
| [03 — Laboratório em Python](03-aula2-laboratorio.md) | Classificação, regressão, métricas e interpretação |
| [04 — PBL Permanência estudantil](04-pbl-permanencia.md) | Proposta de apoio estudantil e cuidados com uso dos dados |
| [05 — Questões de revisão — Maurício](05-revisao-mauricio.md) | Respostas individuais às questões de revisão |
| [06 — Autoavaliação — Maurício](06-autoavaliacao-mauricio.md) | Reflexão sobre aprendizado e dificuldades |

## Código, base e gráficos

- [Notebook com os experimentos executados](notebooks/laboratorio-equipe.ipynb)
- [Base sintética em CSV](dados/educacionais-sinteticos.csv)
- [Resultados numéricos em JSON](evidencias/resultados_execucao.json)
- [Matriz de confusão em PNG](assets/matriz-confusao.png)
- [Gráfico da regressão em PNG](assets/regressao-observado-previsto.png)
- [Logotipo da UDF em PNG](assets/logo-udf.png)

### Gráficos do laboratório

**Classificação — matriz de confusão**

[![Matriz de confusão do modelo de classificação](assets/matriz-confusao.png)](assets/matriz-confusao.png)

**Regressão — comparação entre valores observados e previstos**

[![Valores observados e previstos pelo modelo de regressão](assets/regressao-observado-previsto.png)](assets/regressao-observado-previsto.png)

## Resultados principais

| Métrica | Resultado no teste |
| --- | ---: |
| Classificação — registros de treino / teste | 450 / 150 |
| Acurácia da árvore de decisão | 78,00% |
| Acurácia da referência que prevê a classe mais comum | 59,33% |
| Verdadeiros negativos / falsos positivos / falsos negativos / verdadeiros positivos | 75 / 14 / 19 / 42 |
| Sensibilidade para a classe evasão | 68,85% |
| Regressão — registros de treino / teste | 225 / 75 |
| Erro absoluto médio (MAE) | 28,59 empréstimos por semana |
| MAE da referência | 84,73 empréstimos por semana |
| R² | 0,8774 |

A árvore apresentou resultado melhor que a referência nesse conjunto, mas ainda deixou passar 19 dos 61 casos simulados de evasão no teste. Na regressão, as previsões ficaram próximas dos valores gerados, embora existam erros. Esses resultados são de **dados sintéticos**, não de uma instituição real.

## Como o experimento foi feito

Usamos Python, pandas, NumPy, Matplotlib e scikit-learn. Dividimos os dados em treino e teste, tratamos valores ausentes com um `Pipeline` e utilizamos validação cruzada no conjunto de treino para comparar configurações. Mantivemos o teste separado da escolha inicial dos parâmetros. A semente utilizada foi `42`, e as dependências estão em [requirements.txt](requirements.txt).

## Limitações e cuidado com os dados

As bases foram geradas por simulação, com padrões definidos no próprio código. Por isso, não podemos usar os resultados como prova de que o modelo funcionaria com estudantes reais ou em uma biblioteca de verdade. Para uma aplicação real, seriam necessários dados adequados, avaliação mais ampla, proteção da privacidade e acompanhamento humano das decisões.

## Referências

- Material didático e notebook da disciplina Ciência de Dados e Aprendizado de Máquina, UDF, 2026.2.
- SCIKIT-LEARN. [User Guide](https://scikit-learn.org/stable/user_guide.html).
- SCIKIT-LEARN. [Common pitfalls and recommended practices](https://scikit-learn.org/stable/common_pitfalls.html).
- PANDAS. [User Guide](https://pandas.pydata.org/docs/user_guide/index.html).
- MATPLOTLIB. [Pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html).

## Uso de inteligência artificial

Usamos IA como apoio para estudar os conceitos, revisar a escrita, organizar o código e entender os resultados. As métricas foram obtidas pela execução dos experimentos, e as interpretações fazem parte das atividades desenvolvidas.
