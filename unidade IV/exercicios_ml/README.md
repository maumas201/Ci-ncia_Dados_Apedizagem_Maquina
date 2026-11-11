<img src="assets/logo-udf.jpg" alt="UDF Centro Universitário" width="230">

**Profa. Kadidja Valéria | UDF**  
Ciência de Dados e Aprendizado de Máquina · Sistemas de Informação · 2026.2

# Módulo IV — Atividades de Machine Learning

**Equipe:** Maurício Rafael Oliveira da Silva e Gabriel Silva  
**Turma:** Sistemas de Informação — noturno, quarta-feira

## Apresentação

Este repositório reúne exercícios sobre conceitos de aprendizado de máquina, propostas de investigação de problemas e um laboratório de classificação e regressão em Python. As propostas são didáticas e utilizam situações hipotéticas. A base utilizada no laboratório é **sintética**, sem dados pessoais reais de estudantes.

Os exercícios do grupo estão organizados por atividade. As questões de revisão e autoavaliação estão separadas por estudante, pois representam registros individuais. O arquivo de Gabriel reúne os enunciados, ainda sem respostas próprias.

## Atividades

| Atividade | Conteúdo |
| --- | --- |
| [01 — Conceitos](01-aula1-conceitos.md) | Noções de ML, abordagens supervisionada/não supervisionada e classificação de oito situações |
| [02 — PBL Biblioteca](02-pbl-biblioteca.md) | Diagnóstico proposto, perguntas de negócio, dados e forma de avaliação |
| [03 — Laboratório](03-aula2-laboratorio.md) | Classificação, regressão, métricas, experimentos e interpretação |
| [04 — PBL Permanência](04-pbl-permanencia.md) | Proposta responsável de apoio acadêmico com dados sintéticos |
| [05 — Revisão: Maurício](05-revisao.md) | Doze respostas e cálculos |
| [05 — Revisão: Gabriel](05-revisao-gabriel.md) | Doze questões individuais sem respostas atribuídas |
| [06 — Autoavaliação: Maurício](06-autoavaliacao.md) | Reflexão individual |
| [06 — Autoavaliação: Gabriel](06-autoavaliacao-gabriel.md) | Perguntas individuais para resposta do integrante |

## Base e evidências do laboratório

- [Notebook com os experimentos e saídas](notebooks/laboratorio-equipe.ipynb)
- [Notebook didático disponibilizado como referência](notebooks/laboratorio.ipynb)
- [Dados sintéticos em CSV](dados/educacionais-sinteticos.csv)
- [Resultados registrados em JSON](evidencias/resultados_execucao.json)
- [Matriz de confusão](assets/matriz-confusao.png)
- [Gráfico de regressão: valores reais e previstos](assets/regressao-observado-previsto.png)

### Resultados da execução computacional

| Indicador | Resultado |
| --- | ---: |
| Registros de classificação (treino/teste) | 450 / 150 |
| Acurácia de teste da árvore | 78,00% |
| Acurácia do modelo de referência | 59,33% |
| Verdadeiros negativos, falsos positivos, falsos negativos, verdadeiros positivos | 75, 14, 19, 42 |
| Sensibilidade para evasão | 68,85% |
| Registros de regressão (treino/teste) | 225 / 75 |
| Erro absoluto médio (MAE) | 28,59 empréstimos/semana |
| MAE do modelo de referência | 84,73 empréstimos/semana |
| Coeficiente de determinação (R²) | 0,8774 |

Esses valores descrevem apenas o conjunto fictício e a configuração documentada. Não demonstram desempenho em estudantes ou bibliotecas reais nem validam aplicação institucional. No laboratório, a mediana foi ajustada no treino e a escolha inicial da profundidade utilizou validação cruzada. O teste foi separado para avaliação.

## Reprodutibilidade

O notebook da equipe registra a semente aleatória `42`, as bibliotecas utilizadas, a divisão dos dados e as etapas de preparação, treino e avaliação. O arquivo `requirements.txt` contém as dependências. Os experimentos foram executados em ambiente Python/Jupyter, e as métricas foram registradas no arquivo JSON.

## Organização do grupo e apresentação

Maurício participou da organização inicial das respostas e do estudo dos conceitos com auxílio de IA. Gabriel colabora com a documentação acadêmica da dupla, principalmente no projeto de TCC; nenhuma resposta individual foi atribuída a ele sem seu registro. A apresentação em sala foi prevista em roteiro no [PBL de permanência](04-pbl-permanencia.md).

A professora Kadidja também orienta o TCC da dupla e oferece sugestões nas reuniões de orientação. Essas orientações não são tratadas como avaliação específica destas atividades, pois não foi relatado feedback sobre cada exercício deste módulo.

## Fontes e uso de IA

- Material didático e notebook do Módulo IV, da disciplina Ciência de Dados e Aprendizado de Máquina (UDF, 2026.2).
- [Scikit-learn — User Guide](https://scikit-learn.org/stable/user_guide.html).
- [Scikit-learn — Common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html).
- [Orange Data Mining — Test and Score](https://orangedatamining.com/widget-catalog/evaluate/testandscore/).

**Uso de IA:** ferramentas de inteligência artificial auxiliaram na organização da documentação, na revisão da escrita, na explicação de conceitos, na preparação do código e na análise dos resultados. Os experimentos e seus valores estão registrados para conferência. A interpretação e a apresentação acadêmica permanecem sob responsabilidade dos estudantes.
