![UDF Centro Universitário](assets/logo-udf.png)

**Profa. Kadidja Valéria | UDF**  
Ciência de Dados e Aprendizado de Máquina · Sistemas de Informação · 2026.2

# PBL integrador — Apoio à Permanência

## Identificação

- **Equipe:** Maurício Rafael Oliveira da Silva e Gabriel Silva
- **Curso e turma:** Sistemas de Informação — noturno, quarta-feira
- **Semestre:** 2026.2

## Contexto e questão norteadora

Neste problema, pensamos em como uma faculdade poderia reconhecer sinais de evasão e oferecer apoio aos alunos antes do fim do semestre. Usamos os dados sintéticos do laboratório para testar a ideia, sem fazer previsões sobre estudantes reais.

## Nossa proposta de solução

### 1. Delimitação

- **Problema e público:** identificar, na simulação, alunos que poderiam receber um convite para orientação acadêmica, sem deixar de oferecer ajuda aos demais.
- **Decisão que o resultado pode apoiar:** oferecer **convites voluntários para orientação**, sem punir alunos ou tratar uma previsão como certeza.
- **Definição de evasão, unidade e horizonte:** cada linha representa um aluno fictício. O valor 1 significa evasão ao fim do semestre, e 0 significa permanência. A previsão é feita com informações disponíveis até a quarta semana.

### 2. Perguntas de negócio

1. Considerando informações disponíveis até a quarta semana, conseguimos identificar registros de maior risco simulado com sensibilidade superior a uma referência trivial?
2. Qual seria a quantidade e a consequência dos contatos desnecessários e dos casos não sinalizados, e como oferecer apoio independentemente da classificação?

### 3. Dados necessários

| Dado | Papel no projeto | Disponível quando? | Origem pretendida | Necessidade e risco |
| --- | --- | --- | --- | --- |
| Frequência até a semana 4 | Atributo | Ao final da 4ª semana | Diário acadêmico (real, se autorizado) / simulação | Verificar qualidade e padrões de faltas |
| Nota até a semana 4 | Atributo | Ao final da 4ª semana | Avaliações (real, se autorizado) / simulação | 30 ausências na base fictícia; imputar no treino |
| Entregas até a semana 4 | Atributo | Ao final da 4ª semana | Plataforma acadêmica / simulação | Exigências variam entre disciplinas |
| Evasão ao final do semestre | Alvo binário para o treinamento histórico | Somente no encerramento do semestre | Sistema acadêmico / simulação | Evitar vazamento para previsões antecipadas |
| Indicadores de auditoria por grupos, se justificáveis e autorizados | **Apenas auditoria**, não pressupor uso como atributos | Conforme autorização específica | Processo institucional de avaliação de equidade | Alto risco de privacidade e interpretação indevida; inexistentes nesta base |

**Simulação versus investigação real:** somente os três atributos e o alvo fictício estão no laboratório. Um estudo real exigiria definição institucional de evasão, dados históricos representativos, análise temporal, aprovação e governança de acesso. Nenhuma informação individual real foi fornecida.

### 4. Abordagem e algoritmo

- **Formulação:** classificação supervisionada binária, porque o desfecho histórico tem duas categorias conhecidas. O modelo só sinaliza hipótese de atenção, não diagnóstico.
- **Algoritmo introdutório:** `DecisionTreeClassifier` em pipeline com imputação de mediana; profundidade 5, mínimo 10 por folha, semente 42.
- **Referência simples:** `DummyClassifier(strategy='most_frequent')`.

### 5. Avaliação

- **Preparação, divisão e validação:** 600 registros sintéticos; 450 treino e 150 teste estratificado. Mediana estimada dentro do pipeline. Validação cruzada estratificada em cinco partes do treino; teste reservado para a avaliação final.
- **Métricas e razão da escolha:** acurácia para comparação geral; sensibilidade da classe 1 para identificar evasões; matriz para explicitar falsos negativos e falsos positivos. Acurácia isolada não é suficiente.
- **Resultados do laboratório:** acurácia da árvore **0,7800**, referência **0,5933**; matriz **TN=75, FP=14, FN=19, TP=42**; sensibilidade classe 1 **0,6885**. [Relatório](03-aula2-laboratorio.md) | [Notebook](notebooks/laboratorio-equipe.ipynb).
- **Erros relevantes e consequências:** 19 casos de evasão simulada ficaram sem sinalização (falsos negativos); 14 registros de permanência receberam sinalização indevida (falsos positivos). A abordagem humana deve evitar estigma e garantir acesso aberto a apoio.

### 6. Limites e proteção

**Por que não podemos afirmar uma relação de causa e efeito?** Porque a simulação foi criada com padrões definidos no código. Mesmo em dados reais, um aluno pode faltar por causa de trabalho, transporte ou problemas pessoais. A frequência pode estar relacionada à evasão, mas isso não prova que ela seja a causa.

**Por que os dados sintéticos não são suficientes para usar o sistema na faculdade?** Porque são dados inventados para o exercício. Eles não representam todas as diferenças entre cursos, estudantes e semestres. Para uma aplicação real, precisaríamos fazer outros testes, com autorização e avaliação dos riscos.

**Que grupos poderiam ser mal representados?** Alunos de cursos, turnos e modalidades diferentes podem ter rotinas distintas. A base fictícia não traz informações para comparar esses grupos. Em uma avaliação real, precisaríamos verificar se os erros do modelo são diferentes entre grupos, respeitando privacidade e autorização de uso dos dados.

**Como cuidar dos dados dos alunos?** Usar apenas as informações necessárias, limitar o acesso a profissionais autorizados e definir por quanto tempo os dados serão guardados. Não publicar dados pessoais em repositórios públicos.

**Como garantir revisão humana?** Uma previsão não deve tomar decisões pelo aluno. Profissionais devem analisar cada situação, ouvir o estudante e permitir que ele questione informações incorretas.

### 7. Recomendações de apoio

- **Ação voluntária proposta:** mensagem discreta com convite para orientação de estudos, monitoria, apoio psicopedagógico ou serviços de permanência disponíveis, sem revelar uma "pontuação de risco".
- **Como acolher estudantes não sinalizados:** canais permanentes de atendimento, comunicação ampla de serviços e solicitação espontânea de ajuda; não condicionar acolhimento ao algoritmo.
- **O que verificar antes de aplicação real:** autorização institucional e base legal, definições de desfecho, governança, representatividade, validação temporal independente, avaliação de impactos, processo de contestação, capacidade efetiva de apoio e participação dos estudantes na avaliação.

## Roteiro para apresentação em sala — cinco minutos

| Duração | Tema |
| --- | --- |
| 1 minuto | Problema de evasão, dados fictícios e momento da previsão |
| 2 minutos | Como a árvore foi treinada, divisão dos dados e matriz de confusão |
| 1 minuto | Erros, limitações e riscos de interpretação |
| 1 minuto | Apoio voluntário, privacidade e revisão humana |

Na apresentação, vamos explicar os resultados do exercício e deixar claro que os dados são sintéticos.

[Voltar ao início](README.md).
