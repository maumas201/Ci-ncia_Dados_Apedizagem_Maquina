# Atividade Prática — Detetives dos Dados

## Ciência de Dados e Aprendizagem de Máquina — Aula 01

**Tema:** Introdução à Ciência de Dados e Big Data  
**Metodologia:** Trabalho em equipe  
**Tempo:** 20 minutos  
**Entregável:** Mapa do Problema de Ciência de Dados

---

## 1. Identificação da equipe

| Campo | Resposta |
| --- | --- |
| **Turma:** | Sistemas de Informação |
| **Data:** | 19/08 |
| **Equipe:** | Business Intelligence aplicado à Gestão Hospitalar Pública |
| **Integrante 1:** | Maurício Rafael |
| **Integrante 2:** | Gabriel Silva |
| **Integrante 3:** |  |
| **Integrante 4:** |  |
| **Integrante 5:** |  |

---

## 2. Objetivo da atividade

Nesta atividade, sua equipe deverá analisar um **problema real** e pensar como uma equipe de Ciência de Dados poderia utilizar dados para compreender a situação e apoiar uma decisão.

O objetivo não é desenvolver um sistema ou modelo de Machine Learning neste momento.

O objetivo é aprender a **pensar como um cientista de dados**:

> **Problema → Dados → Informação → Análise → Decisão → Benefício**

---

## 3. Escolha do problema

Escolha uma área para investigar:

* [ ] Comércio
* [ ] Banco
* [x] Saúde
* [ ] Transporte
* [ ] Educação
* [ ] Entretenimento
* [ ] Indústria
* [ ] Meio ambiente
* [ ] Esportes
* [ ] Outra: __________________________

### Problema escolhido

**Descreva, em poucas linhas, o problema que sua equipe pretende analisar.**

> A gestão hospitalar pública utiliza grandes volumes de dados sobre internações, estabelecimentos, leitos, procedimentos e utilização dos serviços de saúde. Entretanto, esses dados podem estar distribuídos em diferentes bases e apresentados de forma pouco intuitiva para quem precisa tomar decisões.
>
> O problema escolhido é a dificuldade de transformar dados públicos de saúde em informações consolidadas e visuais que permitam identificar tendências, diferenças entre unidades ou regiões e possíveis gargalos.
>
> O TCC propõe utilizar Business Intelligence para organizar e visualizar esses dados, inicialmente com foco no Distrito Federal.

---

## 4. Quem possui esse problema?

Identifique a organização, grupo ou público afetado pelo problema.

**Quem possui ou enfrenta esse problema?**

> Gestores de hospitais públicos, gestores das Secretarias de Saúde e profissionais responsáveis pelo planejamento, monitoramento e administração dos serviços hospitalares.

### Quem é afetado pelo problema?

> A administração pública, os profissionais de saúde e, de forma indireta, a população que utiliza o Sistema Único de Saúde, pois decisões de gestão influenciam a organização e a distribuição dos recursos disponíveis.

---

## 5. Por que esse problema é importante?

Explique por que vale a pena investigar esse problema utilizando dados.

**Qual é o impacto do problema?**

> Quando os dados existentes não são transformados em informações claras, os gestores podem ter dificuldade para identificar aumento de internações, diferenças entre regiões, concentração de procedimentos e possíveis desequilíbrios entre demanda e estrutura hospitalar.
>
> Isso pode tornar o processo de decisão mais lento e dificultar a definição de prioridades.
>
> A análise de dados pode ajudar a compreender melhor o cenário hospitalar e fornecer evidências para apoiar o planejamento e a gestão dos recursos públicos.

---

## 6. Qual decisão precisa ser tomada?

Imagine que sua equipe foi contratada para ajudar uma organização.

**Qual decisão a organização precisa tomar?**

> A organização precisa decidir quais unidades, regiões ou indicadores necessitam de maior atenção e onde existem sinais de maior demanda ou possíveis gargalos.
>
> A partir dos resultados, os gestores podem definir prioridades de planejamento, investigar problemas específicos e avaliar a necessidade de redistribuição de recursos ou revisão de processos.

---

# 7. Identificação dos dados

Agora pense:

> **Quais dados seriam necessários para compreender esse problema?**

Liste pelo menos **5 dados**.

| Nº | Dado necessário | Por que esse dado é importante? |
| -: | --- | --- |
| 1 | Quantidade de internações hospitalares | Permite acompanhar a demanda e comparar períodos, unidades ou regiões. |
| 2 | Estabelecimento ou unidade de saúde | Permite identificar onde os atendimentos e internações estão concentrados. |
| 3 | Município ou região do estabelecimento | Permite realizar comparações geográficas e identificar diferenças entre localidades. |
| 4 | Quantidade e tipo de leitos disponíveis | Ajuda a relacionar a estrutura hospitalar disponível com a demanda observada. |
| 5 | Procedimentos e tipos de internação | Permite identificar quais tipos de atendimento apresentam maior volume. |
| 6 | Data ou período da internação | Permite acompanhar tendências e mudanças ao longo do tempo. |
| 7 | Valores relacionados às internações | Permite complementar a análise com informações sobre utilização de recursos financeiros. |

### Exemplos

Podem ser considerados dados como:

* idade;
* localização;
* frequência;
* notas;
* compras;
* valores;
* horários;
* avaliações;
* histórico de utilização;
* registros de atendimento;
* imagens;
* textos;
* localização geográfica.

### Fontes de dados relacionadas ao TCC

> **SIH-SUS/DATASUS:** dados sobre internações hospitalares realizadas no SUS.
>
> **CNES:** dados sobre estabelecimentos de saúde, estrutura e recursos cadastrados.

---

# 8. Que informações queremos descobrir?

Os dados, quando analisados, podem gerar informações úteis.

**O que sua equipe gostaria de descobrir a partir dos dados?**

### Pergunta 1

> Como a quantidade de internações varia ao longo do tempo no Distrito Federal?

### Pergunta 2

> Quais unidades ou regiões apresentam maior concentração de internações e procedimentos?

### Pergunta 3

> Existem diferenças relevantes entre a demanda observada e a estrutura hospitalar disponível?

### Pergunta 4

> Quais indicadores podem ajudar os gestores a identificar tendências ou possíveis gargalos de forma mais rápida?

---

# 9. Quais padrões podemos procurar?

Pense como um cientista de dados.

Sua equipe poderia procurar:

* [x] Tendências
* [x] Comparações
* [x] Grupos semelhantes
* [x] Comportamentos recorrentes
* [x] Valores fora do padrão
* [x] Relações entre variáveis
* [x] Mudanças ao longo do tempo
* [x] Outros: concentração de demanda e possíveis gargalos hospitalares

### Explique um padrão que vocês gostariam de encontrar

> Um padrão importante seria identificar unidades ou períodos em que a quantidade de internações cresce de forma consistente ou se mantém acima das demais unidades.
>
> Também seria útil observar situações em que uma região apresenta alta demanda em comparação com a estrutura hospitalar cadastrada.
>
> Esses padrões poderiam indicar pontos que merecem uma investigação mais detalhada por parte dos gestores.

---

# 10. Qual análise poderia ser realizada?

Como os dados poderiam ser analisados?

Marque uma ou mais possibilidades:

* [x] Análise descritiva
* [x] Comparação entre grupos
* [x] Análise temporal
* [x] Visualização por gráficos
* [x] Identificação de padrões
* [ ] Classificação
* [ ] Previsão
* [ ] Agrupamento
* [x] Outra: construção de indicadores e dashboards de Business Intelligence

### Explique

> Inicialmente, os dados podem ser analisados por meio de estatísticas descritivas, comparações entre unidades e regiões e análise da evolução dos indicadores ao longo do tempo.
>
> Os resultados podem ser apresentados em dashboards com gráficos, tabelas e indicadores que facilitem a interpretação das informações pelos gestores.

---

# 11. Qual decisão poderia ser tomada?

Depois de analisar os dados, imagine que sua equipe encontrou informações importantes.

**Que decisão poderia ser tomada com base nos resultados?**

> Os gestores poderiam priorizar a análise de unidades ou regiões que apresentem maior demanda, crescimento de internações ou possíveis diferenças entre estrutura disponível e utilização dos serviços.
>
> Com base nisso, poderiam avaliar redistribuição de recursos, necessidade de aprofundar a investigação de determinado problema ou revisão do planejamento hospitalar.

---

# 12. Qual seria o benefício?

Qual seria o possível benefício da decisão para a organização ou para as pessoas envolvidas?

> O principal benefício seria tornar o processo de decisão mais rápido, organizado e baseado em evidências.
>
> Os dashboards poderiam facilitar a identificação de tendências e pontos de atenção, melhorar o acompanhamento dos indicadores hospitalares e apoiar uma utilização mais eficiente das informações disponíveis.

---

# 13. Os 5 Vs do Big Data

Analise o problema escolhido pela equipe.

| V | Pergunta | Resposta da equipe |
| --- | --- | --- |
| **Volume** | Existe uma grande quantidade de dados? | Sim. As bases públicas de saúde armazenam grande quantidade de registros de internações, estabelecimentos, procedimentos e estrutura hospitalar. |
| **Velocidade** | Os dados são gerados ou processados rapidamente? | Os dados são gerados continuamente pelos serviços de saúde, embora a disponibilização pública possa ocorrer em períodos específicos de atualização. |
| **Variedade** | Existem diferentes tipos ou formatos de dados? | Sim. Existem dados de internações, estabelecimentos, leitos, procedimentos, localização, datas e valores, provenientes de diferentes bases. |
| **Veracidade** | Os dados podem apresentar erros ou problemas de qualidade? | Sim. Podem existir dados ausentes, inconsistências, registros desatualizados ou diferenças de preenchimento entre unidades e períodos. |
| **Valor** | Os dados podem gerar algum benefício ou apoiar decisões? | Sim. Quando organizados e analisados, podem apoiar o monitoramento e a tomada de decisão na gestão hospitalar. |

### Qual dos 5 Vs é mais relevante para o problema?

> **Valor.**

### Justifique

> O principal objetivo do projeto não é apenas armazenar grandes quantidades de dados, mas transformar dados públicos já existentes em informações úteis para os gestores.
>
> Por isso, o Valor é o aspecto mais importante: o benefício aparece quando os dados são organizados, analisados e apresentados de forma que possam realmente apoiar uma decisão.

---

# 14. Mapa do Problema de Ciência de Dados

Complete o fluxo abaixo:

```text
┌───────────────────────────────┐
│           PROBLEMA            │
│ Dificuldade de transformar    │
│ dados hospitalares em         │
│ informações para a gestão.    │
└───────────────┬───────────────┘
                ↓
┌───────────────────────────────┐
│             DADOS             │
│ SIH-SUS, CNES, internações,   │
│ leitos, unidades, períodos    │
│ e procedimentos.              │
└───────────────┬───────────────┘
                ↓
┌───────────────────────────────┐
│         INFORMAÇÕES           │
│ Tendências, comparações,      │
│ concentração de demanda e     │
│ possíveis gargalos.           │
└───────────────┬───────────────┘
                ↓
┌───────────────────────────────┐
│           ANÁLISE             │
│ Análise descritiva, temporal, │
│ comparativa e visualização    │
│ em dashboards de BI.          │
└───────────────┬───────────────┘
                ↓
┌───────────────────────────────┐
│           DECISÃO             │
│ Definir prioridades e pontos  │
│ que precisam de investigação  │
│ ou intervenção da gestão.     │
└───────────────┬───────────────┘
                ↓
┌───────────────────────────────┐
│          BENEFÍCIO            │
│ Decisões mais rápidas,        │
│ organizadas e baseadas        │
│ em evidências.                │
└───────────────────────────────┘
```

### Resuma cada etapa

**Problema:**

> Dificuldade de transformar dados públicos hospitalares em informações claras e úteis para apoiar a gestão.

**Dados:**

> Dados do SIH-SUS e CNES, como internações, unidades de saúde, leitos, procedimentos, localização e períodos.

**Informação:**

> Indicadores capazes de mostrar tendências, diferenças entre regiões ou unidades e possíveis pontos de atenção.

**Análise:**

> Análise descritiva, temporal e comparativa, com apresentação dos resultados em gráficos, tabelas e dashboards de BI.

**Decisão:**

> Identificar quais unidades, regiões ou indicadores precisam de maior atenção e definir prioridades para a gestão.

**Benefício:**

> Apoiar decisões mais rápidas e fundamentadas, melhorar o acompanhamento dos serviços e facilitar a interpretação dos dados.

---

# 15. Preparação para apresentação

A equipe terá **2 minutos** para apresentar sua proposta.

Organizem a apresentação seguindo esta estrutura:

### 1. Nosso problema

> A gestão hospitalar pública possui muitos dados, mas nem sempre eles estão organizados de forma simples para apoiar a tomada de decisão.

### 2. Precisamos destes dados

> Precisamos de dados sobre internações, estabelecimentos, leitos, procedimentos, regiões, períodos e valores, utilizando principalmente SIH-SUS e CNES.

### 3. Queremos descobrir

> Queremos identificar tendências, diferenças entre unidades e regiões, concentração de demanda e possíveis gargalos.

### 4. Pretendemos analisar

> Pretendemos utilizar análise descritiva, comparação entre grupos, análise temporal e visualizações em dashboards de Business Intelligence.

### 5. A decisão poderia ser

> Os gestores poderiam definir prioridades e identificar unidades ou regiões que precisam de maior atenção ou investigação.

### 6. O benefício esperado é

> Tornar o acompanhamento dos indicadores mais simples e apoiar decisões mais rápidas e baseadas em evidências.

---

# 16. Checklist da equipe

Antes de entregar, confira:

* [x] Definimos um problema real.
* [x] Identificamos quem é afetado pelo problema.
* [x] Explicamos por que o problema é importante.
* [x] Identificamos pelo menos 5 dados necessários.
* [x] Definimos perguntas que queremos responder.
* [x] Identificamos possíveis padrões.
* [x] Indicamos como os dados poderiam ser analisados.
* [x] Definimos uma possível decisão.
* [x] Identificamos o benefício esperado.
* [x] Analisamos os 5 Vs do Big Data.
* [x] Preenchemos o Mapa do Problema.
* [x] Estamos preparados para apresentar em 2 minutos.

---

# 17. Reflexão final

Responda individualmente ou em equipe:

> **Ter muitos dados significa necessariamente tomar boas decisões? Por quê?**

**Resposta:**

> Não. Ter uma grande quantidade de dados não garante uma boa decisão.
>
> Para que os dados sejam úteis, eles precisam ter qualidade, estar relacionados ao problema analisado e ser interpretados corretamente.
>
> Além disso, uma decisão depende do contexto, dos objetivos da organização e da capacidade de transformar os dados em informações úteis.
>
> Por isso, o mais importante não é apenas a quantidade de dados, mas a qualidade da análise e a forma como os resultados são utilizados.

---

## Entrega

### Produto final

A equipe deverá entregar:

**Mapa do Problema de Ciência de Dados**

contendo:

```text
Problema
   ↓
Dados necessários
   ↓
Informações desejadas
   ↓
Análise
   ↓
Decisão
   ↓
Benefício esperado
```

**Formato sugerido:** Markdown, PDF ou documento disponibilizado pelo professor.

**Apresentação:** 2 minutos por equipe.
