<img src="assets/logo-udf.jpg" alt="UDF Centro Universitário" width="230">

**Profa. Kadidja Valéria | UDF**  
Ciência de Dados e Aprendizado de Máquina · Sistemas de Informação · 2026.2

# PBL — Biblioteca em Foco

## Identificação

- **Equipe:** Maurício Rafael Oliveira da Silva e Gabriel Silva
- **Curso e turma:** Sistemas de Informação — noturno, quarta-feira
- **Semestre:** 2026.2

## Situação-problema

Uma biblioteca universitária enfrenta filas em horários específicos e baixa utilização de alguns serviços. A coordenação deseja melhorar o atendimento e planejar recursos. Este é um **cenário didático**, sem dados operacionais reais fornecidos.

**Público-alvo:** estudantes usuários, equipe de atendimento e gestão.

**Questão norteadora:** como os dados podem orientar o planejamento da biblioteca e a oferta de serviços sem identificar ou discriminar seus usuários?

## Investigação e proposta

O recorte proposto é a **organização da capacidade de atendimento por faixa de horário e serviço**. A decisão seria realocar temporariamente atendentes, adaptar horários e testar comunicação de serviços subutilizados, sem tentar identificar estudantes individualmente.

## Canvas da equipe

| Campo | Registro |
| --- | --- |
| Problema e decisão | Identificar faixas de maior espera e serviços pouco utilizados para propor ajustes de equipe, horários e divulgação; decisões condicionadas a dados reais ainda não coletados |
| Público-alvo | Usuários da biblioteca, atendentes e coordenação |
| O que sabemos | Apenas o enunciado informa filas em alguns horários e baixa utilização de certos serviços; não há medição quantitativa fornecida |
| O que precisamos investigar | Volume por horário, tipos de serviço, tempo de espera real, número de atendentes, calendário acadêmico, horários de funcionamento e representatividade dos registros |
| Pergunta de negócio 1 | Em quais faixas de 30 minutos e serviços o tempo mediano de espera supera o limite operacional definido pela gestão? |
| Pergunta de negócio 2 | Quais serviços têm menor utilização e em quais períodos poderiam ser divulgados ou reorganizados? |
| Unidade de análise e período | Agregado **serviço × dia × faixa de 30 minutos**, coletado durante período definido com a equipe, cobrindo dias letivos e semanas de avaliação |
| Atributos, unidades e origem pretendida | Dia da semana, faixa horária, serviço, total de atendimentos, espera em minutos, equipe disponível e calendário; logs operacionais anonimizados/contagens agregadas |
| Alvo e momento em que será conhecido, ou ausência de alvo | Na etapa inicial, não há alvo para treinamento: análise descritiva. Se houver previsão futura, alvo = **número de atendimentos na próxima faixa**, conhecido após o intervalo e previsto antes de seu início |
| Abordagem e justificativa | **Começar pela análise descritiva**, calculando volumes e medianas. Em etapa posterior, regressão supervisionada para demanda por faixa se os registros forem suficientes e estáveis |
| Alternativa sem ML | Gráficos por faixa e serviço, indicadores de espera mediana e testes de escalas de atendimento; essa alternativa pode resolver o problema sem custo de modelagem |
| Como avaliar a proposta | Comparar antes/depois em períodos semelhantes: espera mediana, filas, atendimento e uso por serviço; considerar sazonalidade. Se houver modelo, divisão temporal e MAE contra previsão de referência |
| Privacidade e limitações | Não coletar nomes, matrículas ou dados sensíveis para o diagnóstico; acesso limitado e agregação. Filas variam com calendário, equipe e eventos não medidos; dados ainda inexistentes |

## Organização do trabalho

A resolução foi organizada pela equipe como uma proposta de estudo. Maurício participou da organização das respostas e do estudo dos conceitos com apoio de IA. Gabriel costuma contribuir com a documentação dos trabalhos acadêmicos da dupla, especialmente no TCC. Isso não é apresentado como comprovação de uma tarefa específica executada por ele neste PBL.

## Conclusão da equipe

**Proposta:** realizar um diagnóstico por faixa de atendimento usando dados agregados, testar mudanças simples de escala e divulgação e acompanhar indicadores. Somente se a análise descritiva for insuficiente e existir histórico adequado, avaliar um modelo de previsão de demanda. O projeto pretende melhorar atendimento sem classificar ou perfilar estudantes individualmente.

**Dúvida ainda aberta:** quais serviços podem ser redistribuídos, qual espera seria aceitável e quais logs a biblioteca realmente possui? Essas informações não foram fornecidas.

**Revisão da proposta:** optamos por começar com gráficos e indicadores simples antes de propor ML, pois ainda não existem dados suficientes para justificar um modelo. A professora orienta regularmente o TCC dos integrantes, mas não foi relatado um feedback específico sobre esta atividade.

## Síntese para apresentação de dois minutos

1. **Problema (25 s):** há relatos de filas em alguns horários e uso reduzido de serviços; ainda faltam medições.
2. **Dados (35 s):** propor contagens por serviço e meia hora, tempo de espera e capacidade, evitando identificar usuários.
3. **Método (35 s):** começar com tabelas e gráficos; só estudar previsão de demanda se a análise simples for insuficiente.
4. **Avaliação (25 s):** verificar se espera e organização melhoram em períodos comparáveis; preservar privacidade.

## Síntese

O resultado desta atividade é uma proposta de investigação para um cenário fictício, não um diagnóstico realizado em uma biblioteca real. [Voltar ao início](README.md).