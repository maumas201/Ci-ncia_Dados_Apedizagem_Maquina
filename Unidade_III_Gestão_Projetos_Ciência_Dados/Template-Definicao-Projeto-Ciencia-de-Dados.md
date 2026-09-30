# TEMPLATE — DEFINIÇÃO ATUALIZADA DO PROJETO DE TCC II

## 1. Identificação do projeto

**Título provisório**

Business Intelligence aplicado à gestão hospitalar pública: integração, tratamento e visualização de dados do SIH/SUS e CNES no Distrito Federal.

**Curso**

Sistemas de Informação — Centro Universitário do Distrito Federal (UDF).

**Equipe**

Gabriel Silva dos Santos  
Maurício Rafael Oliveira da Silva

**Professor(a)/Orientador(a)**

A definir.

**Data de elaboração**

30/09/2026.

**Versão**

2.0 — redefinição do projeto para o TCC II.

---

# 2. Visão geral

## 2.1 Resumo do projeto

O projeto propõe o desenvolvimento de um protótipo de Sistema de Informação orientado a dados para integrar, tratar e visualizar informações públicas hospitalares do Distrito Federal. Serão utilizadas principalmente as bases SIH/SUS e CNES. O sistema deverá executar um fluxo reprodutível de extração, preparação, integração e armazenamento dos dados, gerar indicadores hospitalares documentados e disponibilizá-los em um dashboard interativo. O público-alvo é formado por profissionais de planejamento, monitoramento e análise de informações em saúde. O resultado esperado é um protótipo funcional, acompanhado de documentação metodológica, avaliação da qualidade dos dados e validação dos indicadores apresentados.

## 2.2 Declaração do projeto em uma frase

O projeto utilizará dados públicos do SIH/SUS e CNES para integrar e transformar informações hospitalares em indicadores gerenciais visualizados em um dashboard interativo, apoiando profissionais responsáveis pelo monitoramento e planejamento da saúde pública no Distrito Federal.

---

# 3. Contexto e definição do problema

## 3.1 Contexto

O Sistema Único de Saúde produz e disponibiliza grandes volumes de dados públicos por meio de diferentes Sistemas de Informação em Saúde.

Entre essas bases estão o Sistema de Informações Hospitalares do SUS, utilizado para registros relacionados às internações hospitalares, e o Cadastro Nacional de Estabelecimentos de Saúde, que contém informações sobre estabelecimentos, estrutura e leitos.

A disponibilidade dessas bases não significa que sua utilização seja direta.

Os dados apresentam estruturas próprias, diferentes períodos de competência, códigos e formatos que precisam ser compreendidos, preparados e integrados antes da utilização em análises gerenciais.

O desafio deste projeto não está apenas em criar gráficos, mas em construir um processo reprodutível capaz de transformar diferentes fontes públicas em uma camada analítica coerente.

O Distrito Federal será utilizado como recorte inicial para permitir um desenvolvimento controlado e tecnicamente verificável.

## 3.2 Problema central

Profissionais responsáveis por planejamento, monitoramento e análise de informações na saúde pública podem encontrar dificuldade para transformar dados hospitalares públicos provenientes de diferentes sistemas em indicadores integrados e de interpretação gerencial, devido à dispersão das fontes, diferenças de estrutura, necessidade de tratamento e limitações de qualidade dos registros.

## 3.3 Evidências iniciais

| Evidência | Fonte | O que indica | Limitação |
|---|---|---|---|
| Existência de grandes bases públicas hospitalares | DATASUS/SIH | Há dados disponíveis para análise | Disponibilidade não garante facilidade de uso |
| CNES disponibiliza informações sobre estabelecimentos e leitos | CNES | Permite complementar dados hospitalares com informações estruturais | É necessário alinhar competência e código CNES |
| Trabalhos acadêmicos desenvolvem dashboards com SIH/SUS | Literatura recente | A visualização interativa é tecnicamente viável | Fazer apenas outro dashboard teria baixa novidade |
| Trabalhos recentes integram diferentes Sistemas de Informação em Saúde | SBSI 2025 | A integração pode gerar uma contribuição mais relevante | Exige maior atenção à qualidade e compatibilidade das fontes |

---

# 4. Público-alvo e partes interessadas

## 4.1 Público-alvo principal

**Usuários ou beneficiários**

Profissionais responsáveis por planejamento, monitoramento, gestão e análise de informações na saúde pública.

**Necessidades**

Acesso a indicadores consolidados, filtros, comparações temporais e informações provenientes de diferentes bases em uma interface de leitura mais simples.

**Como são afetados pelo problema**

A análise de bases públicas pode exigir manipulação manual, compreensão de códigos específicos, tratamentos repetitivos e consulta a diferentes fontes.

**Que decisões ou ações poderão ser apoiadas**

Identificação de variações temporais, comparação entre estabelecimentos, monitoramento de internações, análise de estrutura hospitalar e identificação de situações que mereçam investigação gerencial.

Importante: o protótipo não toma decisões automaticamente.

## 4.2 Público-alvo secundário

Pesquisadores, estudantes e analistas que trabalham com dados públicos de saúde.

## 4.3 Partes interessadas

| Parte interessada | Interesse | Influência | Envolvimento |
|---|---|---:|---|
| Equipe do TCC | Desenvolvimento e avaliação | Alta | Desenvolvimento |
| Professor orientador | Qualidade acadêmica e técnica | Alta | Orientação |
| Profissionais de gestão/saúde | Utilidade e clareza das informações | Média/Alta | Possível avaliação |
| DATASUS/Ministério da Saúde | Origem dos dados | Alta sobre os dados | Fonte pública |
| UDF | Avaliação acadêmica | Alta | Banca e orientação |

---

# 5. Objetivos do projeto

## 5.1 Objetivo geral

Desenvolver e avaliar um protótipo de Sistema de Informação para integração, tratamento e visualização de dados públicos hospitalares do Distrito Federal, utilizando informações do SIH/SUS e CNES para gerar indicadores gerenciais por meio de um dashboard interativo.

## 5.2 Objetivos específicos

| Nº | Objetivo específico | Evidência de conclusão |
|---:|---|---|
| 1 | Identificar indicadores hospitalares gerenciais que possam ser calculados de forma confiável a partir das bases públicas selecionadas | Catálogo e fórmulas dos indicadores |
| 2 | Extrair, compreender e preparar dados do SIH/SUS e CNES referentes ao Distrito Federal | Bases brutas e relatório exploratório |
| 3 | Desenvolver um processo reprodutível de limpeza, padronização e integração das bases | Pipeline executável |
| 4 | Implementar um dashboard interativo para exploração dos indicadores | Protótipo funcional |
| 5 | Avaliar a consistência dos indicadores, o funcionamento do pipeline e as limitações da solução | Testes e relatório de avaliação |

## 5.3 Verificação dos objetivos

Os objetivos deverão:

- produzir entregáveis verificáveis;
- ser executáveis no período do TCC II;
- utilizar apenas indicadores sustentados pelas bases;
- manter relação direta com o problema central;
- evitar promessas de impacto institucional não comprovado.

---

# 6. Perguntas de negócio

| Nº | Pergunta | Decisão/análise apoiada | Dados necessários | Indicador possível |
|---:|---|---|---|---|
| 1 | Como o volume de internações varia ao longo do tempo? | Monitoramento temporal | SIH | Internações por competência |
| 2 | Quais estabelecimentos concentram maior número de internações? | Comparação entre unidades | SIH + CNES | Internações por CNES |
| 3 | Como os leitos SUS estão distribuídos entre os estabelecimentos? | Análise estrutural | CNES | Leitos por unidade e tipo |
| 4 | Como o tempo médio de permanência varia entre períodos ou estabelecimentos? | Identificação de diferenças relevantes | SIH | Média de permanência |
| 5 | Quais unidades ou períodos apresentam comportamento diferente do padrão observado? | Identificação de pontos para investigação | SIH + CNES | Diferença em relação à média/mediana |

As perguntas não devem produzir diagnósticos automáticos de “bom” ou “ruim”.

O sistema apresentará evidências descritivas para apoiar investigação.

---

# 7. Hipóteses iniciais

## H1

A integração de dados do SIH/SUS e CNES permitirá produzir uma visão mais completa do contexto hospitalar do que a utilização isolada de uma única base.

**Como testar**

Comparar os indicadores disponíveis antes e depois da integração das fontes.

**Resultado que refutaria**

A integração não acrescentar informação analítica relevante ou apresentar incompatibilidades que impeçam seu uso.

## H2

Um pipeline automatizado ou semiautomatizado reduzirá a quantidade de tarefas manuais necessárias para atualizar os indicadores.

**Como testar**

Registrar etapas manuais necessárias na primeira preparação e comparar com execuções posteriores do pipeline.

**Resultado que refutaria**

A necessidade de intervenção manual permanecer praticamente igual.

## H3

A organização dos indicadores em um dashboard facilitará a realização de consultas gerenciais previamente definidas.

**Como testar**

Executar cenários de uso e, se possível, realizar avaliação com usuários ou especialistas.

**Resultado que refutaria**

Os usuários não conseguirem responder às perguntas definidas ou considerarem a visualização pouco clara.

---

# 8. Dados necessários e viabilidade

## 8.1 Fontes

| Fonte | Informações principais | Formato | Acesso | Uso |
|---|---|---|---|---|
| SIH/SUS | Internações, estabelecimento, permanência, valores, procedimentos e período | Microdados públicos | DATASUS/PySUS | Produção hospitalar |
| CNES | Estabelecimentos, leitos, serviços e características estruturais | Microdados públicos | DATASUS/PySUS | Estrutura hospitalar |
| Tabelas auxiliares | Municípios, códigos e descrições | CSV/tabelas públicas | DATASUS/IBGE | Decodificação e enriquecimento |

## 8.2 Unidade de análise

A unidade principal deverá ser:

**estabelecimento hospitalar + competência mensal.**

Isso permite relacionar informações hospitalares com características do estabelecimento no mesmo período.

## 8.3 Recorte territorial

Distrito Federal.

## 8.4 Recorte temporal

Utilizar os **12 meses completos mais recentes disponíveis e considerados suficientemente estáveis na data de extração**.

Caso 2026 esteja incompleto:

- utilizar 2025 ou outro intervalo consolidado como base principal;
- apresentar 2026 apenas como período parcial, se for relevante;
- nunca comparar período parcial com ano completo sem sinalização.

## 8.5 Avaliação inicial dos dados

Antes de desenvolver indicadores, verificar:

- quantidade de registros;
- campos disponíveis;
- valores nulos;
- duplicidades;
- competência;
- códigos CNES;
- correspondência SIH × CNES;
- campos monetários;
- campos de permanência;
- hospitais sem correspondência;
- alterações estruturais entre competências.

## 8.6 Privacidade, ética e segurança

O projeto utilizará bases públicas.

A análise será agregada.

Não haverá tentativa de identificação individual de pacientes.

Nenhum dado deverá ser publicado de forma que permita reidentificação.

Os dados utilizados, período de extração, filtros e transformações devem ser documentados.

---

# 9. Escopo do projeto

## Dentro do escopo

Integração SIH/SUS e CNES.

Recorte inicial no Distrito Federal.

Tratamento e padronização dos dados.

Avaliação da qualidade das bases utilizadas.

Construção de camada analítica.

Cálculo de indicadores descritivos.

Dashboard interativo.

Filtros temporais e por estabelecimento.

Documentação metodológica.

Testes das funções e indicadores.

Avaliação do protótipo.

## Fora do escopo

Inteligência Artificial ou Machine Learning.

Predição de demanda hospitalar.

Diagnóstico clínico.

Recomendação médica.

Decisão automatizada.

Substituição de sistemas institucionais.

Atualização em tempo real.

Análise de dados identificáveis de pacientes.

Cobertura de todo o Brasil na primeira versão.

Implantação oficial em hospital ou secretaria.

---

# 10. Solução proposta

A solução será composta por cinco camadas.

### Camada 1 — aquisição

SIH/SUS e CNES serão obtidos por meio das fontes públicas disponíveis, preferencialmente utilizando PySUS.

### Camada 2 — preparação

Python e Pandas serão utilizados para limpeza, transformação, normalização e seleção dos dados.

### Camada 3 — integração

As informações serão relacionadas principalmente por código CNES e competência temporal.

### Camada 4 — camada analítica

Os dados tratados poderão ser armazenados em arquivos Parquet e consultados com DuckDB.

### Camada 5 — apresentação

Streamlit e Plotly serão utilizados para construir a interface e as visualizações.

Fluxo:

DATASUS/PySUS  
→ dados brutos  
→ validação de qualidade  
→ Pandas  
→ integração SIH + CNES  
→ Parquet/DuckDB  
→ cálculo de indicadores  
→ Streamlit/Plotly  
→ dashboard

---

# 11. Metodologia

## 11.1 Método principal — Design Science Research

O projeto será conduzido como desenvolvimento e avaliação de um artefato tecnológico.

As etapas serão adaptadas para:

1. identificação do problema;
2. definição dos objetivos da solução;
3. projeto e desenvolvimento;
4. demonstração;
5. avaliação;
6. comunicação dos resultados.

O artefato produzido será o protótipo do Sistema de Informação.

## 11.2 Processo de dados — CRISP-DM adaptado

### Compreensão do problema

Definir necessidades, público-alvo e perguntas gerenciais.

### Compreensão dos dados

Conhecer SIH/SUS, CNES, estrutura, período e limitações.

### Preparação dos dados

Limpeza, padronização, integração e transformação.

### Modelagem

Neste projeto, “modelagem” não significa obrigatoriamente Machine Learning.

Corresponderá à organização dos indicadores, agregações, estrutura analítica e regras de cálculo.

### Avaliação

Verificar indicadores, resultados, coerência das consultas e funcionamento do protótipo.

### Implantação

Disponibilização do protótipo em ambiente local ou web acadêmico.

## 11.3 Processo técnico — ETL/ELT

Extract  
→ obtenção dos dados.

Transform  
→ limpeza, padronização e integração.

Load  
→ gravação na camada analítica.

## 11.4 Desenvolvimento incremental

O sistema será desenvolvido em pequenas versões funcionais.

Primeiro:

SIH do DF de uma competência.

Depois:

CNES da mesma competência.

Depois:

integração.

Depois:

12 meses.

Depois:

indicadores.

Por último:

dashboard completo.

---

# 12. Tecnologias

| Tecnologia | Papel |
|---|---|
| Python | Linguagem principal |
| Pandas | Limpeza, transformação e agregação |
| PySUS | Acesso às bases públicas |
| Parquet | Formato eficiente para dados tratados |
| DuckDB | Banco/camada analítica local |
| Streamlit | Aplicação web/dashboard |
| Plotly | Visualizações interativas |
| Git/GitHub | Versionamento e documentação |
| pytest | Testes automatizados |
| VS Code | Desenvolvimento |

## Tecnologia opcional futura

PostgreSQL poderá substituir ou complementar DuckDB caso seja necessário um servidor de banco de dados, acesso simultâneo ou expansão do sistema.

Não é requisito da primeira versão.

---

# 13. Indicadores iniciais candidatos

A inclusão definitiva dependerá da análise das bases.

## Indicadores prioritários

Total de internações.

Internações por mês.

Internações por estabelecimento.

Tempo médio de permanência.

Valor total registrado/aprovado.

Valor médio por internação.

Quantidade de leitos SUS.

Distribuição de leitos por estabelecimento.

Distribuição de leitos por tipo.

## Indicadores secundários

Internações por faixa etária.

Internações por sexo.

Relação entre internações e leitos.

Comparação temporal.

Comparação entre estabelecimentos.

## Indicador sob avaliação

Taxa de ocupação.

Só deverá entrar se os dados disponíveis permitirem uma fórmula metodologicamente adequada.

Não utilizar:

internações / leitos = taxa de ocupação.

Se os dados não sustentarem o cálculo, retirar o indicador.

---

# 14. Resultados e entregáveis previstos

| Entregável | Descrição | Critério de aceite |
|---|---|---|
| Base bruta documentada | Dados obtidos das fontes oficiais | Origem e período registrados |
| Base tratada | Dados limpos e padronizados | Pipeline reproduzível |
| Relatório de qualidade | Problemas encontrados nos dados | Métricas documentadas |
| Base integrada | SIH + CNES | Chaves e competência verificadas |
| Catálogo de indicadores | Fórmula, campos e interpretação | Cada indicador rastreável |
| Pipeline | Extração → preparação → integração → carga | Execução reproduzível |
| Dashboard | Interface interativa | Filtros e gráficos funcionando |
| Testes | Verificação do código e indicadores | Casos principais aprovados |
| Relatório/TCC | Metodologia, resultados e limitações | Coerente com a implementação |

---

# 15. Estratégia de avaliação

## 15.1 Validação de dados

Comparar valores agregados produzidos pelo sistema com consultas oficiais, arquivos originais ou valores de referência disponíveis.

## 15.2 Validação técnica

Criar testes para:

colunas obrigatórias;

tipos de dados;

filtros;

cálculos;

integração;

indicadores;

casos de erro.

## 15.3 Avaliação funcional

Criar cenários de uso.

Exemplo:

“Identifique o estabelecimento com maior número de internações no período selecionado.”

O sistema deverá permitir responder à questão corretamente.

## 15.4 Avaliação com usuários

Se houver disponibilidade, convidar pequeno número de profissionais, professores ou especialistas para avaliar:

clareza;

facilidade de uso;

utilidade percebida;

compreensão dos indicadores.

Caso isso não seja possível, a limitação deverá ser explicitada.

Não inventar validação institucional.

---

# 16. Critérios de sucesso

| Critério | Evidência | Meta |
|---|---|---|
| Qualidade dos dados | Relatório de validação | Problemas identificados e documentados |
| Reprodutibilidade | Execução do pipeline | Nova execução gera os mesmos resultados para os mesmos dados |
| Consistência | Comparação com fonte | Indicadores compatíveis com fonte de referência |
| Funcionalidade | Testes | Principais funcionalidades executam sem erro |
| Usabilidade | Cenários ou avaliação | Usuário consegue localizar indicadores propostos |
| Utilidade | Perguntas de negócio | Dashboard responde às perguntas definidas |

---

# 17. Plano inicial de trabalho

| Etapa | Atividade |
|---|---|
| 1. Definição | Consolidar problema, perguntas e indicadores candidatos |
| 2. Obtenção | Baixar SIH de uma competência do DF |
| 3. Exploração | Conhecer campos e qualidade |
| 4. CNES | Obter mesma competência e avaliar integração |
| 5. Pipeline inicial | Criar limpeza e padronização |
| 6. Integração | Relacionar SIH e CNES |
| 7. Escala | Expandir para 12 meses |
| 8. Indicadores | Implementar fórmulas |
| 9. Camada analítica | Parquet/DuckDB |
| 10. Dashboard | Streamlit + Plotly |
| 11. Testes | Validação técnica e dos dados |
| 12. Avaliação | Cenários e possíveis usuários |
| 13. TCC | Atualizar metodologia e resultados |
| 14. Defesa | Preparar demonstração |

---

# 18. Riscos do projeto

| Risco | Probabilidade | Impacto | Resposta |
|---|---:|---:|---|
| Dados de 2026 incompletos | Alta | Médio | Usar últimos 12 meses completos disponíveis |
| Diferenças entre SIH e CNES | Alta | Alto | Documentar e criar regras de integração |
| Indicador inviável | Média | Médio | Substituir por indicador sustentado pela base |
| PySUS apresentar problema | Média | Médio | Download direto/alternativo |
| Volume de dados elevado | Média | Médio | Parquet + DuckDB + agregação |
| Falta de usuário especialista | Média | Médio | Avaliação técnica e cenários; declarar limitação |
| Escopo crescer demais | Alta | Alto | Priorizar MVP |
| Tempo insuficiente | Média | Alto | Desenvolver incrementalmente |

---

# 19. Organização da equipe

Distribuição proposta, ajustável após definição com o orientador.

**Maurício Rafael**

Pipeline de dados, implementação, banco/camada analítica, dashboard e documentação técnica.

**Gabriel Silva**

Pesquisa bibliográfica, documentação acadêmica, análise dos indicadores e apoio à validação.

**Ambos**

Definição das perguntas, revisão metodológica, testes, interpretação dos resultados, redação e apresentação.

---

# 20. Diferencial científico/técnico esperado

O projeto não será apresentado como apenas mais um dashboard.

O diferencial pretendido será composto por:

integração de duas bases distintas de saúde;

análise de qualidade dos dados;

pipeline reprodutível;

proveniência dos indicadores;

documentação das fórmulas;

visualização interativa;

validação do artefato.

Essa combinação deverá distinguir o trabalho de soluções que utilizam somente uma base e apresentam gráficos sem explicitar o processo de preparação, integração e validação.

---

# 21. Resultado mínimo aceitável

Caso o tempo seja limitado, o projeto só será considerado concluído tecnicamente se possuir:

uma base real do SIH/SUS;

uma base real do CNES;

recorte do Distrito Federal;

integração funcional;

três ou mais indicadores verificados;

pipeline reproduzível;

dashboard funcional;

documentação das limitações;

validação dos principais cálculos.

Qualquer funcionalidade além disso será evolução.

---

# 22. Possível evolução futura

Após o MVP:

atualização automática por competência;

PostgreSQL;

deploy em servidor;

controle de versões dos dados;

mais bases públicas;

mais unidades federativas;

API;

avaliação institucional;

novos indicadores.

Esses itens não fazem parte do núcleo obrigatório do TCC II.

---

# 23. Frase final que deve orientar todo o projeto

O projeto não busca apenas visualizar dados públicos.

Ele busca construir e avaliar um processo reprodutível capaz de integrar dados hospitalares públicos, transformar esses dados em indicadores rastreáveis e disponibilizá-los por meio de uma interface interativa para apoio à análise gerencial.
