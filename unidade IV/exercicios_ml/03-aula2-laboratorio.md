<img src="assets/logo-udf.jpg" alt="UDF Centro Universitário" width="230">

**Profa. Kadidja Valéria | UDF**  
Ciência de Dados e Aprendizado de Máquina · Sistemas de Informação · 2026.2

# Aula 2 — Registro do laboratório supervisionado

## Identificação

- **Equipe:** Maurício Rafael Oliveira da Silva e Gabriel Silva
- **Curso e turma:** Sistemas de Informação — noturno, quarta-feira
- **Semestre:** 2026.2

## Percurso escolhido

- [x] **Python / Jupyter**, com resultados registrados em 11/11/2026.
- [ ] Orange Data Mining — não utilizado.

**Notebook executado:** [notebooks/laboratorio-equipe.ipynb](notebooks/laboratorio-equipe.ipynb). Base de classificação com **600 registros fictícios** e alvo `evasao_fim_semestre` (0 permaneceu, 1 evadiu). Relações simuladas: não há inferência sobre estudantes reais.

## 1. Ambiente e reprodução

| Item | Registro |
| --- | --- |
| Ambiente e data | Python 3.13.5, execução computacional em ambiente Jupyter/Python, 11/11/2026 |
| Versões das ferramentas/bibliotecas | NumPy 2.3.5; pandas 2.2.3; Matplotlib 3.10.8; scikit-learn 1.8.0 |
| Semente aleatória | `42` (geração, divisão e modelos) |
| Caminho do notebook executado ou fluxo Orange | `notebooks/laboratorio-equipe.ipynb` |
| Origem dos dados e condição sintética | Gerados pelo notebook fornecido; CSV de apoio `dados/educacionais-sinteticos.csv`; registros inteiramente fictícios |

## 2. Problema e preparação

- **Pergunta de negócio:** quais registros fictícios apresentariam maior sinal de evasão ao fim do semestre, para orientar eventual convite voluntário de apoio?
- **Unidade de análise e horizonte:** um estudante fictício; atributos até a **4ª semana**, resultado ao final do semestre.
- **Atributos disponíveis no instante da previsão:** `frequencia_sem4`, `nota_sem4`, `entregas_sem4`.
- **Variável-alvo e sua natureza:** `evasao_fim_semestre`, binária/categórica (0/1).
- **Ausências e outros problemas encontrados:** 30 valores ausentes em `nota_sem4` (5% dos 600 registros); não foram detectadas ausências nas outras três colunas. Não há indicação de registros reais; a construção da base impõe associações artificiais.
- **Tratamentos e conjunto usado para aprendê-los:** imputação pela **mediana ajustada apenas nos subconjuntos de treino**, dentro de `Pipeline`, sem calcular mediana no teste ou em dobras de validação.

## 3. Desenvolvimento e teste

- **Método de divisão e justificativa:** `train_test_split(test_size=0.25, stratify=y, random_state=42)`; estratificação conserva aproximadamente a proporção das classes. Usado porque os registros da simulação são independentes; dados reais exigiriam testes temporais e controle de repetição por estudante.
- **Quantidades de treino e teste:** 450 e 150 registros.
- **Procedimento de validação no treino:** `StratifiedKFold`, cinco dobras, embaralhamento e semente 42; seleção por acurácia média.
- **Parâmetros da árvore e como foram escolhidos:** profundidade comparada em 2, 3, 5 e sem limite, com `min_samples_leaf=10`. Profundidade **5** obteve maior acurácia média da validação (**0,7222**, desvio padrão **0,0391**). Os experimentos posteriores com folhas diferentes foram apenas exploratórios; não modificaram a árvore final.
- **Como o teste ficou fora da seleção:** escolha inicial da profundidade pela validação de treino; avaliação com 150 registros reservados. Após o teste, as análises adicionais foram restritas a treino/validação, sem nova seleção baseada nos resultados do teste.

**Fluxo e método de avaliação realmente utilizados:** `SimpleImputer(median)` → `DecisionTreeClassifier(max_depth=5, min_samples_leaf=10, random_state=42)` em `Pipeline`, comparado a `DummyClassifier(strategy='most_frequent')`. O Orange não foi utilizado.

## 4. Resultados calculados de classificação

| Modelo | Configuração | Acurácia de treino | Acurácia de validação e dispersão | Acurácia de teste |
| --- | --- | --- | --- | --- |
| Referência | Classe mais frequente (`DummyClassifier`) | 0,5889 | 0,5889 ± 0,0000 | **0,5933** |
| Árvore final | Profundidade 5; folha mínima 10; imputação mediana | **0,8133** (ajuste final) | **0,7222 ± 0,0391** (5 dobras) | **0,7800** |

A coluna de validação é **média ± desvio padrão entre dobras**, sem representar um intervalo de confiança.

**Matriz de confusão (linhas reais, colunas previstas; classe positiva 1):**

| Real / previsto | Permaneceu (0) | Evadiu (1) |
| --- | --- | --- |
| Permaneceu (0) | **75** (TN) | **14** (FP) |
| Evadiu (1) | **19** (FN) | **42** (TP) |

![Matriz de confusão](assets/matriz-confusao.png)

- **Acurácia calculada manualmente pela matriz:** `(75 + 42)/(75 + 14 + 19 + 42) = 117/150 = 0,7800` = **78%**.
- **Sensibilidade da classe 1:** `42/(42+19) = 0,6885` = **68,85%**; 19 dos 61 casos reais simulados de evasão não foram sinalizados.
- **Precisão adicional da classe 1:** `42/(42+14) = 0,7500` = **75%**.
- **Comparação com referência:** a árvore melhora a acurácia de teste em **18,67 pontos percentuais** (78,00% menos 59,33%), neste único conjunto sintético; não comprova benefício institucional.
- **Consequências dos falsos positivos:** estudantes que permaneceriam poderiam receber abordagem desnecessária ou sofrer estigma, sobretudo se o alerta for usado de forma inadequada.
- **Consequências dos falsos negativos:** pessoas que poderiam precisar de apoio ficariam sem contato proativo. Deve existir atendimento acessível mesmo para quem não for sinalizado.
- **Interpretação do gráfico e da árvore:** o modelo separa registros sintéticos por limiares de desempenho e participação na semana 4. A diferença entre treino (**81,33%**) e validação (**72,22%**) sugere investigar sobreajuste/variabilidade; não permite concluir causalidade.

## 5. Experimentos no treino

Os experimentos seguintes usam **apenas treino/validação** e não mudam a configuração final já avaliada no teste.

| Experimento | Alteração | Resultado de validação | Interpretação |
| --- | --- | --- | --- |
| 1 | Profundidade 5, folhas mínimas **5, 10, 20 e 40** | Respectivamente **0,7222; 0,7222; 0,7267; 0,7289** | Folhas maiores restringem complexidade; o melhor número isolado não basta para uma nova escolha após consultar o teste |
| 2 | Retirar somente `nota_sem4` (profundidade 5; folhas 10) | **0,6289**, contra **0,7222** com todos os atributos | A nota contribuiu à predição nessa simulação, mas isso não prova relação causal |

**Dispersões do experimento 1:** para 5, 10, 20 e 40, desvios padrão = 0,0298; 0,0391; 0,0480; 0,0303, respectivamente. Outros testes de remoção de atributos estão no notebook.

**1. Como a profundidade e o tamanho das folhas podem afetar o sobreajuste?** Profundidades muito grandes e folhas muito pequenas podem ajustar ruídos específicos do treino. Limitar profundidade ou aumentar mínimo de registros por folha tende a regularizar, porém limites excessivos causam subajuste. Comparar médias e dispersões da validação é mais consistente do que olhar a acurácia de treino.

**2. Retirar um atributo e observar mudança no desempenho prova causalidade?** Não. A diferença indica utilidade preditiva naquele conjunto. O atributo pode estar correlacionado com outras variáveis ou ser resultado de fatores não medidos.

**3. Se 95% permanecem, o que acontece com um modelo que sempre prevê permanência?** Ele tem **95% de acurácia** e **0% de sensibilidade para evasão**: não identifica nenhum caso positivo. A matriz revelaria todos os evadidos como falsos negativos.

## 6. Regressão — seção independente

| Item | Registro |
| --- | --- |
| Atributos e alvo | `usuarios_ativos` e `horas_abertura`; alvo numérico `emprestimos_semana` |
| Divisão e preparação | 300 registros fictícios; 225 treino e 75 teste (`test_size=0.25`, semente 42); pipeline com imputação de mediana e regressão linear |
| MAE do modelo e unidade | **28,59 empréstimos/semana** no teste |
| MAE da referência | **84,73 empréstimos/semana** para `DummyRegressor(strategy='mean')` |
| R² do teste | **0,8774** |
| Interpretação do gráfico observado/previsto | Pontos relativamente próximos à diagonal, mas com dispersão; são erros da previsão para casos sintéticos |
| Interpretação dos resíduos | Resíduos `real - previsto` de ambos os sinais; média no teste ≈ **-1,28** empréstimos/semana, dispersão padrão ≈ **35,47**; sem garantia de padrão equivalente em dados reais |
| Limitação de extrapolação | Os usuários ativos foram gerados na faixa de 100 a 1.000; prever 10.000 usuários extrapola além do domínio observado |

![Gráfico observado/previsto](assets/regressao-observado-previsto.png)

**Experimento adicional:** validação cruzada apenas no treino com os dois atributos resultou em MAE médio **28,89**; apenas usuários ativos **35,90**; apenas horas de abertura **83,73**. Os valores não demonstram efeito causal de abertura ou usuários.

**Por que R² não é porcentagem de acertos?** O R² compara a soma dos erros quadráticos do modelo com o erro de uma referência que prevê a média do conjunto avaliado. Seu valor pode ser negativo e não mede proporção de previsões individuais corretas. O valor 0,8774 neste teste não significa "87,74% dos empréstimos previstos corretamente".

## 7. Evidências e conclusão

- Notebook executado: [notebooks/laboratorio-equipe.ipynb](notebooks/laboratorio-equipe.ipynb).
- Resultados estruturados: [evidencias/resultados_execucao.json](evidencias/resultados_execucao.json).
- Imagens: [matriz de confusão](assets/matriz-confusao.png) e [regressão](assets/regressao-observado-previsto.png).
- **Principal aprendizado técnico:** treinamento, validação e teste têm funções diferentes; uma boa acurácia pode ocultar falsos negativos e um R² alto não significa previsão sem erro.
- **Limitações de generalização e vieses possíveis:** dados artificialmente gerados, relação entre atributos imposta na simulação, uma amostra e uma divisão de teste, ausência de verificação por subgrupos reais e possíveis mudanças ao longo do tempo.
- **Cuidados com privacidade e uso responsável:** minimizar dados, restringir acesso, evitar perfis discriminatórios, revisar decisões humanas, garantir contestação e não aplicar esse modelo sintético em estudantes reais.

**Nota sobre reprodução:** executar no Colab/Jupyter pode gerar pequenos desvios entre versões. O arquivo mostra resultados da execução local. Se modificar o modelo a partir do que aprendeu no teste, uma nova avaliação final exigirá conjunto independente.

[Voltar ao início](README.md).
