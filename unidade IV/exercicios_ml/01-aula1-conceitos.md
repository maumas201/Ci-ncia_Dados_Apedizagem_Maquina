![UDF Centro Universitário](assets/logo-udf.png)

**Profa. Kadidja Valéria | UDF**  
Ciência de Dados e Aprendizado de Máquina · Sistemas de Informação · 2026.2

# Aula 1 — Conceitos e classificação de problemas

## Identificação

- **Equipe:** Maurício Rafael Oliveira da Silva e Gabriel Silva
- **Curso e turma:** Sistemas de Informação — noturno, quarta-feira
- **Semestre:** 2026.2

## Objetivos

Distinguir programação tradicional e Machine Learning, identificar atributos e alvo e diferenciar classificação, regressão e agrupamento.

## 1. Explicação com suas palavras

**1. Como um modelo aprende com dados?**

Ele aprende analisando os dados e identificando padrões neles. Com esses padrões, o algoritmo vai ajustando o modelo, que depois consegue fazer previsões, classificações e outras análises com novos dados.

**2. Qual diferença entre algoritmo e modelo?**

O algoritmo é usado para analisar os dados e identificar padrões, seguindo um processo de treinamento. Já o modelo é o resultado desse treinamento, que pode ser utilizado para fazer previsões ou classificações com novos dados.

**3. Compare uma regra de bloqueio de palavra com um modelo de spam.**

A regra de bloqueio usa palavras definidas previamente, sem aprender com exemplos. Já o modelo de spam analisa vários e-mails, tanto spam quanto mensagens normais, para aprender padrões e conseguir diferenciar um do outro. Mesmo assim, os dois podem cometer erros.

**4. Dê um exemplo de atributo e alvo e defina o momento da previsão.**

Eu usaria como exemplo a previsão de evasão de um aluno. Os atributos seriam a frequência, as notas e as atividades entregues até a quarta semana. O alvo seria saber se o aluno evadiu ou permaneceu no curso no fim do semestre. A previsão aconteceria na quarta semana, usando só os dados disponíveis naquele momento.

**IA, Ciência de Dados e Machine Learning:** Entendi que a IA é a área mais ampla. A Ciência de Dados usa dados, estatística e programação para entender problemas e apoiar decisões. Já o Machine Learning usa algoritmos para aprender padrões com exemplos. Um gráfico de frequência, por exemplo, é uma análise de dados; usar esses registros para treinar um modelo que prevê evasão é Machine Learning.

## 2. Quadro comparativo

| Critério | Supervisionado | Não supervisionado |
| --- | --- | --- |
| Presença de alvo no treino | Sim, exemplos com resposta conhecida | Não há alvo rotulado para a tarefa |
| Pergunta que pode responder | Qual o resultado esperado para um novo caso? | Quais padrões, grupos ou estruturas existem? |
| Tipo de saída | Categoria ou valor numérico previsto | Grupos, componentes, padrões ou anomalias |
| Tarefas e exemplo | Classificação de spam; regressão de empréstimos | Agrupamento de hábitos de acesso |
| Dados necessários | Atributos e um alvo confiável nos registros de treino | Atributos relevantes, mesmo sem rótulos |
| Forma de avaliação | Acurácia, sensibilidade, MAE, R², conforme tarefa, em dados separados | Coesão/separação de grupos, estabilidade e utilidade do padrão; eventualmente avaliação por especialistas |
| Limitação | Dependência de rótulos e risco de sobreajuste e vazamento | Grupos podem não ter significado útil; avaliação costuma ser menos direta |

## 3. Situações-problema

Analisamos os oito casos propostos, para comparar as diferenças entre classificação, regressão e agrupamento.

| Caso escolhido | Alvo ou ausência de alvo | Categoria, quantidade ou grupos? | Abordagem e justificativa | Dados necessários e limitação |
| --- | --- | --- | --- | --- |
| 1 — Educação | `evadiu/permaneceu` (rótulo conhecido no histórico) | Categoria binária | Supervisionado: **classificação** | Frequência, notas e entregas disponíveis antes da previsão; pode haver vieses e informações incompletas |
| 2 — Saúde | Tempo de espera em minutos | Quantidade | Supervisionado: **regressão** | Horário, demanda e capacidade da unidade; mudanças operacionais reduzem generalização |
| 3 — Comércio | Sem categorias anteriores de clientes | Grupos | Não supervisionado: **agrupamento** | Histórico de compras agregado; grupos dependem de medidas, escala e escolha de algoritmo |
| 4 — Finanças | `inadimplente/adimplente` | Categoria binária | Supervisionado: **classificação** | Dados anteriores à concessão e desfechos confiáveis; risco de discriminação e vazamento |
| 5 — Segurança digital | `spam/legítima` | Categoria binária | Supervisionado: **classificação** | Mensagens rotuladas e atributos de texto; spammers mudam estratégias |
| 6 — Comércio | Vendas em reais na próxima semana | Quantidade | Supervisionado: **regressão** | Histórico de vendas, sazonalidade, feriados; requer avaliação temporal |
| 7 — Educação | Sem rótulo de evasão para a tarefa | Grupos | Não supervisionado: **agrupamento** | Frequência e padrões de acesso; perfis não equivalem a risco comprovado |
| 8 — Saúde | Categoria do exame, definida por especialistas | Categoria | Supervisionado: **classificação** | Exames rotulados e representativos; erros clínicos exigem supervisão profissional |

## 4. Raciocínio crítico

**“Detectar fraude” define sozinho o tipo de aprendizado?** Não, porque depende dos dados disponíveis. Se tivermos exemplos já identificados como fraude ou não fraude, podemos usar classificação supervisionada. Se não houver esses exemplos, podemos tentar identificar transações fora do padrão, usando detecção de anomalias. Mas uma operação diferente não significa necessariamente fraude. Por isso, antes de escolher o método, precisamos entender os dados, o objetivo e o que pode acontecer quando o sistema erra.

[Voltar ao início](README.md).
