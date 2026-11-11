<img src="assets/logo-udf.jpg" alt="UDF Centro Universitário" width="230">

**Profa. Kadidja Valéria | UDF**  
Ciência de Dados e Aprendizado de Máquina · Sistemas de Informação · 2026.2

# Questões de revisão — Maurício Rafael Oliveira da Silva

## Identificação

- **Equipe:** Maurício Rafael Oliveira da Silva e Gabriel Silva
- **Curso e turma:** Sistemas de Informação — noturno, quarta-feira
- **Semestre:** 2026.2

As questões numéricas 6 e 7 são exemplos propostos no exercício, diferentes das métricas calculadas no laboratório.

## 1. Explique a diferença entre regra programada para bloquear uma palavra e modelo de spam treinado com exemplos.

**Resposta:** Uma regra usa uma condição fixa, como bloquear qualquer e-mail que tenha uma palavra. Já o modelo de spam aprende com vários exemplos de mensagens e tenta identificar padrões para diferenciar spam de e-mail normal. Os dois podem errar.

## 2. Por que codificar evadiu/permaneceu como 1/0 não transforma classificação em regressão?

**Resposta:** Mesmo usando 0 e 1, o alvo ainda representa duas categorias: evadiu e permaneceu. Por isso é classificação, não regressão. O número é só uma forma de representar a classe.

## 3. Uma biblioteca quer estimar empréstimos e descobrir perfis. Que tarefas correspondem a cada pergunta?

**Resposta:** Para estimar a quantidade de empréstimos, podemos usar regressão, porque queremos prever um número. Para descobrir grupos de usuários com hábitos parecidos, podemos usar agrupamento, sem precisar ter grupos definidos antes.

## 4. O que são atributo, alvo e unidade de análise no laboratório educacional?

**Resposta:** Cada linha representa um aluno fictício, que é a unidade de análise. Os atributos são frequência, nota e entregas até a quarta semana. O alvo é a evasão ou permanência no fim do semestre.

## 5. Por que calcular a mediana antes de dividir os dados pode invalidar a avaliação?

**Resposta:** Porque, ao calcular a mediana de todos os dados antes da divisão, acabamos usando informações do teste no treinamento. Isso pode melhorar o resultado de forma artificial. O correto é separar treino e teste primeiro e calcular a mediana usando apenas o treino.

## 6. Em uma matriz didática com TN=80, FP=5, FN=10, TP=5, calcule acurácia e sensibilidade. O resultado é suficiente para aprovar o modelo?

**Resposta:** O total é 80 + 5 + 10 + 5 = 100. A acurácia é (80 + 5) / 100 = **85%**. A sensibilidade é 5 / (5 + 10) = **33,33%**. Mesmo com 85% de acurácia, o modelo deixou de identificar 10 dos 15 casos positivos. Então não dá para aprová-lo olhando só a acurácia.

## 7. Valores reais 100, 120, 140 e previsões 110, 115, 130. Calcule MAE e informe a unidade se o alvo for vendas em reais.

**Resposta:** Primeiro calculamos os erros absolutos: 10, 5 e 10. Depois fazemos a média: (10 + 5 + 10) / 3 = **R$ 8,33**. Isso significa que, nesse exemplo, as previsões erraram em média R$ 8,33.

## 8. Um R² de -0,2 significa “20% de acertos negativos”? Explique.

**Resposta:** Não. O R² não mostra porcentagem de acertos. Ele compara os erros do modelo com os de uma previsão simples que usa a média. Um R² de -0,2 indica que o erro quadrático do modelo foi 20% maior do que o dessa referência.

## 9. Uma árvore tem acurácia 1,00 no treino e 0,65 na validação. Que hipótese investigar e como?

**Resposta:** Uma possibilidade é o sobreajuste: a árvore ficou muito boa nos dados de treino, mas não teve o mesmo resultado em dados diferentes. Eu verificaria a profundidade, o tamanho mínimo das folhas e os resultados da validação, além de possíveis problemas nos dados.

## 10. Por que escolher a profundidade pelo teste prejudica a estimativa final?

**Resposta:** Porque o teste deveria ser usado apenas no final, para avaliar o modelo em dados que não influenciaram a escolha. Se usamos o teste para escolher a profundidade, acabamos ajustando o modelo a ele, e o resultado pode parecer melhor do que realmente é.

## 11. Baixa frequência associada à evasão demonstra causa? Proponha explicação alternativa.

**Resposta:** Não. A baixa frequência pode estar associada à evasão sem ser a causa direta. Por exemplo, problemas de transporte ou trabalho podem fazer o aluno faltar mais e também aumentar a chance de abandonar o curso.

## 12. Um modelo sinaliza um estudante como possível evasão. Que ação responsável pode ser adotada?

**Resposta:** O ideal seria oferecer uma conversa ou apoio acadêmico de forma reservada e voluntária. A previsão não é uma certeza e não deveria ser usada para punir o aluno. Também é importante oferecer apoio para quem não foi sinalizado pelo modelo.

## Referências e apoio utilizado

- Material didático e notebook do Módulo IV, disponibilizados pela disciplina.
- SCIKIT-LEARN. *User Guide*. https://scikit-learn.org/stable/user_guide.html.
- SCIKIT-LEARN. *Common pitfalls and recommended practices*. https://scikit-learn.org/stable/common_pitfalls.html.

As respostas foram organizadas e revisadas com apoio de inteligência artificial. A interpretação das questões e o acompanhamento dos exemplos fazem parte do estudo individual.

[Voltar ao início](README.md).
