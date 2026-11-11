<img src="assets/logo-udf.jpg" alt="UDF Centro Universitário" width="230">

**Profa. Kadidja Valéria | UDF**  
Ciência de Dados e Aprendizado de Máquina · Sistemas de Informação · 2026.2

# PBL integrador — Apoio à Permanência

## Identificação

- **Equipe:** Maurício Rafael Oliveira da Silva e Gabriel Silva
- **Curso e turma:** Sistemas de Informação — noturno, quarta-feira
- **Semestre:** 2026.2

## Contexto e questão norteadora

Uma instituição deseja reconhecer sinais associados à evasão e oferecer apoio antes do final do semestre. O laboratório do módulo usa somente dados sintéticos. **Nenhum resultado autoriza classificar estudantes reais.**

## Proposta de solução

### 1. Delimitação

- **Problema e público:** identificar, em simulação, estudantes que poderiam receber oferta de orientação acadêmica e apoio, mantendo acesso universal a serviços de acolhimento.
- **Decisão que o resultado pode apoiar:** priorizar **convites voluntários de conversa** com profissionais; não aplicar sanções, negar matrícula, cortar bolsa ou concluir que alguém vai evadir.
- **Definição de evasão, unidade e horizonte:** neste exercício, cada linha é um estudante fictício; 1 indica evasão ao término do semestre e 0, permanência. No mundo real, regras administrativas de evasão e exclusão precisam ser definidas formalmente antes de coletar dados. Previsão após a semana 4.

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
- **Resultados efetivamente calculados e evidência:** acurácia da árvore **0,7800**, referência **0,5933**; matriz **TN=75, FP=14, FN=19, TP=42**; sensibilidade classe 1 **0,6885**. [Relatório](03-aula2-laboratorio.md) | [Notebook](notebooks/laboratorio-equipe.ipynb).
- **Erros relevantes e consequências:** 19 casos de evasão simulada ficaram sem sinalização (falsos negativos); 14 registros de permanência receberam sinalização indevida (falsos positivos). A abordagem humana deve evitar estigma e garantir acesso aberto a apoio.

### 6. Limites e proteção

**Por que resultados não demonstram causalidade?** Os dados foram gerados por fórmula com relações predeterminadas. Mesmo em registros reais, notas e frequência podem estar associadas a condições externas não medidas e não constituir causas demonstradas da evasão.

**Por que dados sintéticos não validam uso institucional?** Não refletem necessariamente a distribuição de estudantes, diferenças entre cursos e semestres, processos administrativos, características sociais nem efeitos de intervenções; não foram avaliados em população real.

**Que grupos podem ser mal representados? Como investigar?** Poderiam existir diferenças por curso, turno, modalidade e contextos de acessibilidade, mas **a base não contém informações suficientes para afirmar esse tipo de disparidade**. Uma auditoria real dependeria de autorização adequada, justificativa de variáveis, qualidade amostral, métricas por grupo, discussão de privacidade e revisão institucional.

**Como minimizar dados, restringir acesso e definir retenção?** Usar somente informações essenciais e previamente justificadas; aplicar acesso por função, trilhas de auditoria e política de exclusão em prazo definido pelo controlador de dados; não publicar dados reais em repositório público. Prazo exato não pode ser fixado sem política institucional.

**Como garantir revisão humana e contestação?** Nenhuma medida desfavorável pode ocorrer automaticamente. Um profissional autorizado interpreta contexto, verifica divergências, escuta o estudante e oferece canal simples de revisão/contestação, além de registrar correções.

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

A apresentação é parte do planejamento da equipe. Os resultados apresentados são exclusivamente da simulação.

## Organização da equipe

Maurício organizou as respostas e o estudo inicial das atividades com apoio de IA. Gabriel contribui habitualmente com a documentação acadêmica do grupo, especialmente no TCC. A participação específica dele neste PBL não é descrita como uma atividade já executada.

[Voltar ao início](README.md).
