![UDF Centro Universitário](assets/logo-udf.png)

**Profa. Kadidja Valéria | UDF**  
Ciência de Dados e Aprendizado de Máquina · Sistemas de Informação · 2026.2

# PBL — Biblioteca em Foco

## Identificação

- **Equipe:** Maurício Rafael Oliveira da Silva e Gabriel Silva
- **Curso e turma:** Sistemas de Informação — noturno, quarta-feira
- **Semestre:** 2026.2

## Situação-problema

A situação apresentada é de uma biblioteca universitária que tem filas em alguns horários e serviços pouco utilizados. Nossa ideia é entender quando essas filas acontecem e quais mudanças poderiam melhorar o atendimento. Como o exercício não apresenta registros reais da biblioteca, elaboramos uma proposta de investigação.

## Proposta

Escolhemos analisar os atendimentos por dia, horário e tipo de serviço. Primeiro usaríamos tabelas e gráficos para descobrir os horários com maior espera. Com essas informações, poderíamos propor ajustes na escala dos atendentes ou melhorar a divulgação de serviços menos procurados.

## Canvas da equipe

| Campo | Nossa proposta |
| --- | --- |
| Problema e decisão | Entender em quais horários há mais filas e quais serviços são menos usados, para melhorar a organização do atendimento |
| Público-alvo | Estudantes que usam a biblioteca, atendentes e coordenação |
| O que sabemos | O enunciado menciona filas e serviços com baixa procura, mas não apresenta números de atendimentos |
| O que precisamos investigar | Quantos atendimentos acontecem por horário, quanto tempo as pessoas esperam, quais serviços procuram e quantos funcionários estão disponíveis |
| Pergunta de negócio 1 | Em quais horários o tempo de espera é maior? |
| Pergunta de negócio 2 | Quais serviços são menos utilizados e poderiam ser mais divulgados? |
| Unidade de análise e período | Cada serviço em um dia e intervalo de 30 minutos; o levantamento precisaria incluir dias letivos e períodos de prova |
| Atributos, unidades e origem pretendida | Dia da semana, horário, tipo de serviço, número de atendimentos, tempo de espera em minutos e funcionários disponíveis; registros da biblioteca, se disponíveis |
| Alvo e momento da previsão | Na análise inicial, não precisamos de alvo, porque queremos descrever o atendimento. Se depois fizermos previsão, o alvo pode ser o número de atendimentos da próxima faixa de horário |
| Abordagem e justificativa | Começar com análise descritiva. Só considerar regressão para prever demanda quando houver histórico suficiente |
| Alternativa sem ML | Gráficos de movimento por horário, comparação de tempo de espera e mudança na escala de atendimento |
| Como avaliar | Comparar o tempo de espera e o número de atendimentos antes e depois das mudanças, em períodos semelhantes; se houver previsão, comparar o MAE com uma referência simples |
| Privacidade e limitações | Trabalhar com contagens por horário e serviço, sem precisar guardar nomes ou matrículas. Precisaríamos considerar feriados, provas e mudanças na equipe |

## Análise e conclusão

Acho melhor começar com gráficos e indicadores mais simples, porque ainda não sabemos quais dados a biblioteca possui. Não faz sentido treinar um modelo só porque estamos estudando Machine Learning. Se os gráficos mostrarem um padrão de movimento e a biblioteca tiver um histórico confiável, podemos testar um modelo para estimar a demanda.

Também precisamos definir com a coordenação qual tempo de espera seria considerado aceitável. Sem esse parâmetro e sem dados reais, a atividade fica como uma proposta, não como uma avaliação de uma biblioteca existente.

## Resumo para apresentação

1. **Problema:** filas em alguns horários e serviços que são pouco procurados.
2. **Dados:** total de atendimentos, tempo de espera, horário e número de atendentes.
3. **Método:** começar com tabelas e gráficos; avaliar previsão de demanda se houver necessidade.
4. **Avaliação:** comparar os indicadores antes e depois de uma mudança, sem identificar usuários.

[Voltar ao início](README.md).
