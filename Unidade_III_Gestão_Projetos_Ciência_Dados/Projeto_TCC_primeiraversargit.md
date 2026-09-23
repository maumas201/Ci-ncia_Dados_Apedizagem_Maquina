# Definição do Projeto de Ciência de Dados

**Business Intelligence na análise hospitalar do Distrito Federal: organização de dados públicos e proposta de dashboard gerencial**

**Instituição:** Centro Universitário do Distrito Federal - UDF  
**Curso:** Sistemas de Informação  
**Autores:** Gabriel Silva dos Santos e Maurício Rafael Oliveira da Silva  
**Local e data:** Brasília, 21 de setembro de 2026  
**Entregável:** Documento de definição do projeto

## 1. Identificação do projeto

| Campo | Preenchimento |
|---|---|
| Título provisório do projeto | Business Intelligence na análise hospitalar do Distrito Federal: organização de dados públicos e proposta de dashboard gerencial. |
| Curso / disciplina | Sistemas de Informação / Trabalho de Conclusão de Curso. |
| Turma | A informar no registro acadêmico. |
| Equipe | Gabriel Silva dos Santos e Maurício Rafael Oliveira da Silva. |
| Integrantes e funções iniciais | Gabriel: levantamento documental e conferência dos dados. Maurício: organização da base e visualizações. Análise, interpretação e redação: ambos. Distribuição proposta para execução. |
| Professor(a) | Professora Kadidja - orientação. |
| Data de elaboração | 21/09/2026. |
| Versão do documento | 1.0 - definição consolidada do projeto. |

## 2. Visão geral

### 2.1 Resumo do projeto

Dados públicos hospitalares distribuídos entre diferentes bases exigem tratamento para apoiar a análise gerencial. O projeto tem como público principal gestores e equipes de planejamento hospitalar do Distrito Federal. Propõe organizar e integrar dados do SIH/SUS e do CNES para analisar internações, média de permanência e leitos SUS cadastrados. O resultado esperado é uma base documentada, uma análise descritiva e um painel demonstrativo com indicadores, filtros, gráficos e tabelas. A proposta busca facilitar comparações e identificar situações que mereçam investigação, sem substituir a avaliação dos gestores nem presumir ganhos de eficiência.

### 2.2 Declaração do projeto em uma frase

> Nosso projeto utilizará dados públicos do SIH/SUS e do CNES para compreender a distribuição das internações, da permanência hospitalar e dos leitos SUS cadastrados no Distrito Federal, apoiando gestores na priorização de análises sobre a produção hospitalar e a estrutura disponível.

## 3. Contexto e definição do problema

### 3.1 Contexto

A existência de dados públicos não garante sua utilização imediata. Bases administrativas podem apresentar estruturas, códigos e critérios temporais diferentes, exigindo preparação antes da comparação. Saldanha, Bastos e Barcellos (2019) discutem o acesso e o pré-processamento de microdados do DATASUS, oferecendo fundamento para separar obtenção, tratamento e análise dos dados [1].

No contexto hospitalar, o SIH/SUS registra produção relacionada às internações financiadas pelo SUS, enquanto o CNES descreve características dos estabelecimentos e dos leitos cadastrados [2-3]. Reunir essas informações exige definir quais hospitais, períodos e indicadores podem ser comparados. Internações do SUS não abrangem automaticamente toda a produção hospitalar do DF; estabelecimentos privados conveniados também podem participar desse universo.

A SES-DF já publica painéis sobre leitos cadastrados e produção hospitalar [4-5]. Portanto, a contribuição proposta é demonstrar um processo documentado de organização e análise, com recorte explícito e indicadores verificáveis. Não se pressupõe que o governo careça de dashboards. A revisão de Rabiei e Almasi (2022) reforça a necessidade de considerar requisitos de informação, facilidade de uso e integração na concepção de painéis hospitalares [6].

O estudo interessa a gestores e equipes de planejamento que precisam consultar informações comparáveis. Sua relevância está na distância entre a disponibilidade das bases e sua leitura gerencial. A dificuldade concreta dos usuários do DF será tratada como necessidade a validar, pois este projeto não apresenta entrevistas ou medições de uso já realizadas.

### 3.2 Problema central

Gestores e equipes de planejamento hospitalar do Distrito Federal precisam reunir e interpretar informações de produção e estrutura hospitalar publicadas em bases distintas, o que exige compatibilizar conceitos, unidades e períodos antes de realizar comparações confiáveis para o planejamento.

**Pergunta de pesquisa:** como organizar e apresentar dados públicos de internações, permanência hospitalar e leitos SUS cadastrados de modo a tornar sua leitura gerencial mais clara, preservando os limites de interpretação das fontes?

### 3.3 Evidências iniciais

| Evidência | Fonte | O que ela indica? | Confiabilidade / limitação |
|---|---|---|---|
| Produção hospitalar e cadastro de leitos são divulgados em sistemas distintos. | DATASUS e CNES [2-3]. | A análise conjunta requer compatibilização. | Fontes oficiais; finalidade administrativa e diferenças temporais precisam ser consideradas. |
| A SES-DF mantém painéis de leitos e produção hospitalar. | InfoSaúde-DF [4-5]. | Visualizações já integram a comunicação pública de informações de saúde. | A existência do painel não comprova melhoria da gestão nem satisfação dos usuários. |
| A literatura identifica requisitos e desafios na construção de dashboards hospitalares. | Rabiei e Almasi (2022) [6]. | A apresentação visual depende de qualidade dos dados, conteúdo e adequação ao usuário. | Revisão internacional; não demonstra o efeito de um painel específico no DF. |

## 4. Público-alvo e partes interessadas

### 4.1 Público-alvo principal

| Aspecto | Descrição |
|---|---|
| Quem são os usuários ou beneficiários? | Gestores hospitalares e equipes de planejamento e informação em saúde do DF. Pesquisadores e estudantes são beneficiários secundários. |
| Quais necessidades possuem? | Localizar indicadores, conhecer sua origem, comparar unidades compatíveis e reconhecer limitações dos dados. |
| Como são afetados pelo problema? | Precisam conciliar consultas separadas e interpretar conceitos que podem parecer equivalentes, embora representem fenômenos diferentes. |
| Que decisão ou ação poderão tomar com os resultados? | Selecionar unidades e indicadores para investigação, solicitar detalhamento aos serviços e subsidiar discussões sobre produção e planejamento da estrutura hospitalar. |

**Exemplo de uso gerencial:** uma permanência média mais elevada pode motivar análise dos fluxos de atendimento e do perfil assistencial. O indicador isolado não demonstra demora evitável, desperdício ou necessidade de reduzir leitos. Decisões de contratação, expansão ou redistribuição exigem informações operacionais e clínicas adicionais.

### 4.2 Partes interessadas

| Parte interessada | Interesse no projeto | Influência | Forma de envolvimento |
|---|---|---|---|
| Gestores e equipes de planejamento | Clareza e pertinência dos indicadores. | Alta | Perfil de usuário de referência; avaliação prática, se houver disponibilidade e autorização institucional. |
| SES-DF e Ministério da Saúde | Uso correto e contextualizado das informações públicas. | Média | Documentação e bases oficiais; sem parceria institucional presumida. |
| Orientadora e banca | Coerência metodológica, viabilidade e integridade acadêmica. | Alta | Revisão do escopo, dos critérios e das interpretações. |
| Autores | Execução, aprendizagem e conclusão do trabalho. | Alta | Coleta, tratamento, análise, documentação e apresentação. |

## 5. Objetivos do projeto

### 5.1 Objetivo geral

Analisar dados públicos de internações, média de permanência e leitos SUS cadastrados em hospitais do Distrito Federal, mediante organização, integração e visualização em um painel demonstrativo de BI, para apoiar a leitura gerencial da produção e da estrutura hospitalar.

### 5.2 Objetivos específicos

| Nº | Objetivo específico | Evidência de conclusão |
|---:|---|---|
| 1 | Delimitar o universo hospitalar e um período comum às fontes SIH/SUS e CNES. | Protocolo com competência, filtros, unidades incluídas e exclusões justificadas. |
| 2 | Preparar uma base analítica com rastreabilidade das transformações e das limitações. | Arquivos de origem, base tratada, dicionário e registro de qualidade. |
| 3 | Descrever internações, permanência média e leitos SUS por estabelecimento. | Tabelas e gráficos conferidos com as fontes e respostas às perguntas de negócio. |
| 4 | Fundamentar os requisitos do painel a partir de soluções públicas, ferramentas de visualização e documentação de contratação. | Mapeamento comparativo e requisitos vinculados a fontes. |
| 5 | Produzir e verificar um painel demonstrativo com dados reais do recorte. | Indicadores, filtro por hospital, tabelas e roteiro de verificação preenchido. |

### 5.3 Verificação dos objetivos

- [x] São específicos e escritos com clareza.
- [x] Podem ser verificados por meio de entregáveis ou métricas.
- [ ] A viabilidade de extração e compatibilização foi confirmada na coleta inicial.
- [x] Estão diretamente relacionados ao problema central.
- [x] Consideram os usuários e a decisão que será apoiada.

## 6. Perguntas de negócio

| Nº | Pergunta de negócio | Decisão apoiada | Dados necessários | Análise ou indicador possível |
|---:|---|---|---|---|
| 1 | Como as internações registradas se distribuem entre os hospitais do recorte? | Selecionar unidades para examinar a concentração da produção. | Hospital, competência e internações. | Total e participação de cada hospital. |
| 2 | Como varia a média de permanência entre as unidades? | Priorizar investigações sobre perfis e fluxos assistenciais. | Média de permanência e identificação hospitalar. | Comparação descritiva, sem ranking de eficiência. |
| 3 | Como os leitos SUS cadastrados se distribuem entre os hospitais? | Apoiar a leitura da estrutura hospitalar cadastrada. | Hospital, competência, tipo e quantidade de leitos. | Total e composição dos leitos. |
| 4 | Que situações merecem investigação ao observar produção, permanência e estrutura em conjunto? | Selecionar perguntas para análise gerencial aprofundada. | Três indicadores compatibilizados por hospital. | Tabela comparativa e descrição de contrastes. |
| 5 | Quais limitações dos dados afetam as comparações e precisam aparecer no painel? | Decidir se uma comparação é utilizável ou exige revisão. | Correspondências, ausências e notas das fontes. | Cobertura da integração e registro de inconsistências. |

## 7. Hipóteses iniciais

As hipóteses orientam a exploração do recorte e não antecipam resultados nem relações causais.

| Hipótese | Como poderá ser testada? | Resultado que a refutaria? |
|---|---|---|
| H1. As internações não se distribuem de maneira uniforme entre as unidades incluídas. | Comparar contagens e participações no total. | Contagens iguais entre as unidades do recorte. |
| H2. A média de permanência difere entre os hospitais analisados. | Comparar o indicador segundo a precisão publicada e contextualizar o perfil assistencial. | Ausência de diferenças na precisão disponível. |
| H3. A ordenação dos hospitais pelo número de leitos SUS difere da ordenação por internações. | Comparar as duas ordenações, registrando empates e unidades sem correspondência. | Ordenações coincidentes em todas as unidades comparáveis. |

Não serão empregados testes de significância para transformar essas descrições em conclusões sobre causalidade, qualidade assistencial ou eficiência. Uma hipótese refutada também constitui resultado válido.

## 8. Dados necessários e viabilidade

| Conjunto ou fonte de dados | Variáveis principais | Formato | Acesso / responsável | Qualidade esperada |
|---|---|---|---|---|
| SIH/SUS, por local de internação [2] | Identificação do estabelecimento, competência de processamento, internações e permanência média. | Tabulação oficial exportada; CSV ou planilha, conforme opção disponível. | DATASUS / Ministério da Saúde. | Dados administrativos sujeitos a atualização e critérios próprios de contabilização. |
| CNES - recursos físicos e leitos [3] | Código CNES, nome, localização, tipo de estabelecimento, competência e leitos SUS. | Tabulação ou arquivo oficial exportado. | Ministério da Saúde e gestores responsáveis pelo cadastro. | Cadastro de estrutura; não equivale à disponibilidade operacional em tempo real. |
| Documentação e painéis públicos [4-8] | Indicadores publicados, fontes, organização da informação e requisitos documentados. | Páginas oficiais, artigos e documentos. | SES-DF, Ministério da Saúde e autores. | Evidência documental; funções não verificadas serão identificadas como não confirmadas. |

### 8.1 Avaliação inicial dos dados

- **Disponibilidade:** existem canais públicos para consulta. A possibilidade de obter identificação hospitalar e os três indicadores no mesmo recorte será verificada na primeira etapa de coleta.
- **Volume e período coberto:** o núcleo mínimo utilizará uma competência mensal comum às duas fontes, escolhida pela disponibilidade e documentação. O número de estabelecimentos e a competência serão registrados após a extração. Uma série de 12 meses será uma extensão, caso haja dados e tempo para conferência.
- **Dados ausentes, duplicados ou inconsistentes previstos:** códigos inválidos, nomes diferentes para a mesma unidade, registros ausentes, totais indevidamente incluídos como observações e duplicidade de chaves na base analítica.
- **Necessidade de integração entre fontes:** utilizar o código CNES e a competência como chaves, mantendo as unidades não correspondidas no relatório de qualidade. Evitar vinculação automática apenas pelo nome.
- **Restrições legais, contratuais ou institucionais:** utilizar dados públicos agregados, respeitar condições de acesso e atribuição das fontes e observar as exigências acadêmicas e éticas da instituição. Não estão previstos dados internos de hospitais ou credenciais de terceiros.

**Delimitação do universo:** estabelecimentos hospitalares situados no DF e presentes no recorte de produção do SUS. O cadastro será utilizado para conferir localização e caracterização. Hospitais privados conveniados não serão classificados como públicos apenas por registrarem produção SUS. A conclusão abrangerá as unidades efetivamente incluídas, com relação das exclusões.

**Compatibilidade temporal:** o mês de processamento do SIH pode diferir do mês da internação ou da alta [2]. A utilização da mesma competência do CNES organiza a comparação administrativa, mas não transforma os registros em um censo diário de ocupação.

### 8.2 Privacidade, ética e segurança

Compromissos a verificar durante a execução:

- [ ] A equipe verificou se há dados pessoais ou sensíveis nos arquivos obtidos.
- [ ] A coleta e o uso estão limitados à finalidade declarada.
- [ ] O acesso a arquivos de trabalho foi organizado entre os responsáveis.
- [ ] Variáveis pessoais desnecessárias foram excluídas.
- [ ] Possíveis vieses e impactos das comparações foram examinados.
- [ ] A divulgação evita reidentificação ou exposição indevida.

**Cuidados específicos:** trabalhar com agregados por estabelecimento; não divulgar registros individuais de pacientes; evitar cruzamentos que permitam identificá-los; não interpretar ausência como zero; não atribuir desempenho inferior a um hospital com base apenas em valores brutos. Se houver participação de gestores em entrevistas ou testes, o procedimento dependerá da orientação ética institucional aplicável antes da coleta.

**Uso de inteligência artificial:** houve utilização de ChatGPT, da OpenAI, na organização desta proposta, na redação preliminar e no levantamento inicial de referências. O trabalho acadêmico deverá registrar as ferramentas e finalidades efetivamente utilizadas em todas as etapas. Aos autores caberão a execução da análise, a conferência das fontes, a interpretação e a revisão substantiva do texto. A declaração de uso não substitui essas responsabilidades.

O item 3.4 e o Anexo D do Edital UDF nº 30/2026 exigem transparência sobre IA e responsabilidade humana pelo conteúdo. O anexo veda apresentar conteúdo integralmente gerado por IA como autoria própria. Não estabelece um percentual de IA permitido. A submissão exige a declaração institucional preenchida de acordo com o uso real, sem alegar validações ou atividades não realizadas [18].

### 8.3 Procedimentos de preparação e análise

O fluxo de BI será organizado em cinco etapas: obtenção, tratamento, integração, análise e visualização. A limpeza dos dados ocorre antes da apresentação; os filtros do dashboard selecionam recortes da base preparada.

| Etapa | Procedimento | Registro de verificação |
|---|---|---|
| Obtenção | Salvar exportações oficiais e registrar consulta, data, filtros e competência. | Arquivos originais preservados e protocolo de extração. |
| Tratamento | Padronizar códigos e tipos numéricos; separar ausências de zeros; retirar linhas de totais da base por hospital. | Dicionário e registro das transformações. |
| Integração | Agregar cada fonte na granularidade definida antes da junção, evitando multiplicação de registros. | Uma linha por hospital e competência na tabela principal; lista de não correspondências. |
| Análise | Produzir contagens, participações e comparações descritivas; investigar valores discrepantes sem apagá-los automaticamente. | Tabelas de conferência e respostas às cinco perguntas. |
| Visualização | Apresentar indicadores, gráficos, tabela detalhada e filtros, com fonte, competência e notas metodológicas. | Roteiro de uso e reprodução das consultas selecionadas. |

**Dicionário mínimo dos indicadores:**

| Indicador | Definição e apresentação | Limite de interpretação |
|---|---|---|
| Internações | Utilizar o indicador oficial do SIH no recorte; apresentar total e distribuição por hospital [2]. | Não equivale a pacientes únicos nem à contagem indistinta de todas as AIHs. |
| Média de permanência | Utilizar o indicador oficial em dias; registrar a regra de cálculo da tabulação escolhida [2]. | Não calcular média simples das médias hospitalares. Para um total, consultar o agregado oficial correspondente. |
| Leitos SUS cadastrados | Somar categorias não sobrepostas do CNES no estabelecimento e competência selecionados [3]. | Não representa leitos livres ou ocupados no momento da consulta; leitos complementares têm particularidades cadastrais. |
| Participação nas internações | Internações do hospital divididas pelo total do recorte, multiplicadas por 100. | Descreve concentração da produção registrada, sem medir demanda reprimida. |
| Cobertura da integração | Hospitais com correspondência no CNES divididos pelos hospitais elegíveis do SIH, multiplicados por 100. | Expressa correspondência entre bases, não cobertura de toda a assistência do DF. |

Não será calculada taxa de ocupação por meio da divisão dos dias de permanência do SIH pelos leitos cadastrados. As notas técnicas alertam que esses dias podem incluir períodos externos ao mês de processamento [2]. Também não serão somados estoques mensais de leitos como se fossem unidades diferentes.

## 9. Escopo do projeto

| Dentro do escopo | Fora do escopo |
|---|---|
| Um recorte mensal de produção SUS e estrutura hospitalar cadastrada no DF. | Representar toda a produção privada não financiada pelo SUS ou medir ocupação em tempo real. |
| Tratamento, integração, documentação e análise descritiva de dados públicos. | Previsão de demanda, diagnóstico clínico e decisão automatizada. |
| Painel demonstrativo, tabelas e gráficos com dados reais conferidos. | Implantação em ambiente governamental de produção ou integração com prontuários. |
| Mapeamento dirigido de soluções e requisitos para fundamentar o painel. | Revisão sistemática exaustiva ou avaliação comercial de todas as plataformas. |
| Verificação de consistência e clareza da apresentação. | Comprovar redução de custos, melhoria assistencial ou impacto causal na gestão. |

**Restrições conhecidas:** prazo curto, disponibilidade das exportações, compatibilidade entre competências, conhecimento técnico, licenças eventualmente necessárias e ausência de acesso garantido a gestores para avaliação.

### 9.1 Enquadramento acadêmico e modalidade

O projeto caracteriza-se como **pesquisa aplicada, exploratória e descritiva, com abordagem quantitativa sobre dados secundários**, apoiada por pesquisa bibliográfica e documental. A contribuição central será o processo reproduzível de organização e análise dos dados e sua comunicação em um painel.

O formato de definição de projeto comporta implementação de código: objetivos, dados, etapas, critérios de aceite e riscos orientam tanto uma aplicação programada quanto uma solução construída em ferramenta de BI. A presença de código não determina, isoladamente, a modalidade científica.

| Modalidade do Edital UDF | Adequação ao projeto |
|---|---|
| Artigo científico | Enquadramento preferencial, desde que apresente método executado, resultados próprios e discussão dos limites. |
| Revisão de literatura | Exigiria colocar a síntese da literatura no centro do objetivo. Não é o enquadramento escolhido. |
| Estudo de caso | Seria apropriado se o trabalho investigasse uma unidade ou implantação delimitada, com procedimento de estudo de caso. Usar dados do DF, por si só, não basta. |
| Relato de experiência | Exigiria uma experiência efetivamente realizada e analisada; não se sustenta apenas com uma proposta de desenvolvimento. |

Na tabela de áreas do CNPq, **Sistemas de Informação - 1.03.03.04-9** é um enquadramento temático compatível [17]. A classificação de área não substitui a escolha da modalidade de publicação.

### 9.2 Soluções públicas de saúde e contribuição para o projeto

| Solução | Utilização documentada | Contribuição para o projeto | Limite da evidência |
|---|---|---|---|
| InfoSaúde-DF: leitos cadastrados [4] | Publicação de painel sobre leitos, com acesso a relatório em Power BI. | Referência local para apresentação de estrutura hospitalar e indicação da fonte. | A página pública não demonstra o processo interno de implantação nem o impacto gerencial. |
| InfoSaúde-DF: produção hospitalar [5] | Publicação de painel de produção de serviços, com acesso a relatório em Power BI. | Referência local para comunicação de produção hospitalar. | Não se atribuem filtros específicos sem verificação direta do relatório. |
| Sala de Apoio à Gestão Estratégica - SAGE [7] | Disponibilização de informações e painéis para apoiar a gestão em saúde. | Fundamenta a utilização governamental de informações organizadas para acompanhamento. | Finalidade institucional declarada não equivale a avaliação de efetividade. |
| CNES 360, do Conass [8] | Plataforma para consultar e visualizar informações de estabelecimentos de saúde. | Exemplo de exploração de dados cadastrais e estrutura da rede. | Conass é uma entidade representativa de secretários estaduais; o exemplo não deve ser tratado como contratação da SES-DF. |

### 9.3 Mapeamento de ferramentas de visualização

O quadro compara características documentadas e adequação ao escopo. Não constitui teste de desempenho nem demonstra que uma ferramenta é superior em qualquer contexto.

| Ferramenta | Características e relação com saúde | Adequação ao projeto | Condição ou limitação |
|---|---|---|---|
| Power BI [11] | Preparação, modelagem e relatórios interativos; uso identificado nos acessos dos painéis da SES-DF [4-5]. | Opção principal para a entrega mínima, pela construção visual de relatórios. | Medidas, relacionamentos e publicação exigem configuração; verificar licença e forma de compartilhamento. |
| Tableau [12] | Visualização interativa; o fornecedor apresenta aplicações em saúde. | Alternativa para exploração visual dos mesmos indicadores. | Não será exigida uma segunda implementação; condições de uso devem ser verificadas. |
| Qlik [13] | Plataforma analítica com aplicações documentadas pelo fornecedor para saúde. | Referência para comparação de recursos de exploração. | Material do fornecedor não é evidência independente de impacto. |
| Apache Superset [14] | Plataforma aberta para exploração e dashboards sobre fontes de dados. | Alternativa para uma evolução com infraestrutura própria. | Configuração, hospedagem e manutenção acrescentam esforço ao prazo inicial. |
| Streamlit e Plotly [15-16] | Construção de aplicações e gráficos em Python; ferramentas de uso geral. | Caminho para a implementação programada do mesmo painel. | Exige código, ambiente configurado e verificação funcional; não é requisito do núcleo mínimo. |

**Escolha proposta:** produzir o painel mínimo no Power BI, sem desenvolvimento de uma aplicação própria. Caso a execução inicial revele impedimento de acesso, utilizar planilha com tabelas dinâmicas, gráficos e filtro por estabelecimento, registrando a ferramenta adotada. A construção em Python será uma extensão do mesmo modelo de dados e dos mesmos requisitos, sem alterar o problema de pesquisa.

### 9.4 Como requisitos de implantação aparecem no setor público

A contratação pública exige transformar a necessidade em requisitos verificáveis. No âmbito federal dos órgãos integrantes do SISP, a IN SGD/ME nº 94/2022 organiza o planejamento de contratações de TIC, incluindo estudo técnico preliminar e termo de referência. Seu âmbito não deve ser estendido automaticamente à SES-DF ou a todos os municípios [9].

Como exemplo documental específico, o termo de referência de software de saúde de Lebon Régis/SC, de 2025, inclui recursos de BI, filtros e condições de implantação e capacitação. Ele evidencia requisitos solicitados em uma contratação, sem comprovar que a solução foi entregue ou produziu os resultados esperados [10].

| Dimensão observada | Adaptação como requisito do projeto |
|---|---|
| Necessidade e usuários | Relacionar cada visualização a uma pergunta de negócio. |
| Dados e integração | Identificar fonte, competência, granularidade, chaves e regras de atualização. |
| Funcionalidades | Consultar indicadores e filtrar hospitais; disponibilizar tabela detalhada. |
| Qualidade e transparência | Explicitar definições, ausências, origem e data de extração. |
| Entrega e aceite | Conferir os resultados com a fonte e demonstrar consultas previstas. |
| Implantação e uso | Documentar instalação ou abertura do arquivo, dependências e instruções de utilização. |

Esses requisitos são uma adaptação acadêmica fundamentada nos documentos consultados. Não representam um edital da SES-DF nem uma solicitação institucional de contratação deste projeto.

## 10. Resultados e entregáveis previstos

| Entregável | Descrição | Formato | Responsável | Critério de aceite |
|---|---|---|---|---|
| Base tratada | Dados compatibilizados por hospital e competência, acompanhados de dicionário e registro de qualidade. | CSV ou planilha e documentação. | Maurício; conferência de Gabriel. | Chave única na tabela principal e transformações rastreáveis. |
| Análise exploratória | Respostas às cinco perguntas de negócio, com limites de interpretação. | Tabelas, gráficos e texto. | Ambos. | Valores reproduzíveis a partir da base e coerentes com a consulta oficial. |
| Visualizações / painel | Visão geral, comparação por hospital e tabela detalhada, com filtro e notas das fontes. | Arquivo de BI ou planilha interativa; imagens para o texto. | Maurício. | Três indicadores centrais conferidos e filtro por hospital funcionando. |
| Relatório ou apresentação | Método, resultados obtidos, discussão, conclusões e referências. | Documento e apresentação acadêmica. | Ambos. | Distingue evidências, interpretações e limitações; responde à pergunta de pesquisa. |
| Mapeamento e requisitos | Soluções públicas, ferramentas e requisitos aplicáveis ao painel. | Quadros comparativos. | Gabriel. | Cada afirmação externa relevante possui fonte identificável. |
| Extensão com código | Automação da preparação e aplicação em Streamlit/Plotly, se viável. | Código, dependências e instruções. | Maurício; revisão conjunta. | Reproduz os indicadores do núcleo mínimo em ambiente documentado. |

**Resultado esperado:** um produto analítico verificável que facilite localizar e comparar informações hospitalares. O ganho de clareza será examinado por tarefas de consulta e revisão da apresentação. Na ausência de avaliação com usuários do público-alvo, a conclusão ficará limitada à consistência técnica e ao potencial de uso, sem afirmar utilidade gerencial comprovada.

**Distinção entre as entregas:** o núcleo mínimo exige dados reais, análise e visualização funcional em ferramenta existente. Um desenho de tela sem dados pode apoiar o planejamento, mas não substitui esses resultados. A extensão com Python acrescenta automação e personalização; não é necessária para caracterizar a pesquisa como artigo científico.

## 11. Critérios de sucesso

| Critério | Indicador ou evidência | Meta | Forma de verificação |
|---|---|---|---|
| Relevância para o problema | Perguntas de negócio respondidas. | Cinco respostas fundamentadas, inclusive quando a resposta evidenciar limitação. | Relacionar pergunta, resultado e interpretação. |
| Qualidade dos dados | Rastreabilidade e integridade das chaves. | Todos os arquivos identificados; nenhuma duplicidade não resolvida na chave final. | Conferência do protocolo e da base. |
| Qualidade da análise | Correspondência com consultas oficiais. | Três indicadores centrais conferidos; diferenças justificadas. | Comparar o total do recorte e pelo menos três hospitais, ou todos se houver menos de três. |
| Utilidade para o público-alvo | Capacidade de realizar consultas previstas. | Executar três tarefas: localizar internações, comparar permanência e consultar leitos. | Roteiro por revisor acadêmico; registrar se houve ou não participação de gestores. |
| Comunicação dos resultados | Clareza, fontes e limites visíveis. | Todas as telas com competência e fonte; todos os indicadores definidos. | Inspeção do painel e revisão do texto. |

## 12. Plano inicial de trabalho

O cronograma abaixo organiza a execução até 28/09/2026, prazo de submissão aos Cadernos do UDF indicado na retificação do edital [19]. Esse prazo editorial não substitui o calendário de avaliação do TCC. As datas são metas de trabalho, não registros de atividades concluídas.

| Etapa | Atividades principais | Responsável(is) | Prazo | Dependências |
|---|---|---|---|---|
| 1. Definição | Validar objetivo, recorte, indicadores e modalidade. | Ambos e orientadora. | 21/09 | Revisão desta definição. |
| 2. Obtenção dos dados | Confirmar exportações, competência comum e universo; salvar fontes. | Gabriel e Maurício. | 21-22/09 | Acesso e granularidade disponíveis. |
| 3. Preparação dos dados | Tratar, integrar e documentar qualidade; fixar o recorte. | Maurício; revisão de Gabriel. | 22-23/09 | Fontes compatíveis. |
| 4. Análise / modelagem | Produzir indicadores, painel mínimo e interpretações descritivas. | Ambos. | 23-25/09 | Base conferida; modelo de dados definido. |
| 5. Validação | Comparar com consultas oficiais e executar tarefas do painel. | Ambos e revisor disponível. | 25-26/09 | Resultados e painel disponíveis. |
| 6. Comunicação | Finalizar texto, referências, declarações e apresentação; preparar eventual submissão. | Ambos e orientadora. | 26-28/09 | Validação, revisão de autoria e requisitos editoriais. |

**Controle de viabilidade:** até 22/09, confirmar acesso e compatibilidade. Se a integração por hospital não for possível, restringir o recorte a unidades com correspondência verificável e declarar a cobertura. Se nem esse recorte sustentar os três indicadores, revisar formalmente o escopo com a orientadora. Não preencher lacunas com dados inventados nem apresentar resultados esperados como resultados obtidos. A extensão em Python só avançará após estabilização do núcleo mínimo.

## 13. Riscos do projeto

| Risco | Probabilidade | Impacto | Estratégia de resposta | Responsável |
|---|---|---|---|---|
| Falha de acesso ou incompatibilidade entre exportações. | Média | Alto | Testar obtenção no início; reduzir recorte com justificativa e preservar arquivos consultados. | Ambos. |
| Contagem incorreta ou junção que multiplique registros. | Média | Alto | Definir granularidade antes da integração e reconciliar indicadores com a fonte. | Maurício. |
| Prazo insuficiente para concluir a aplicação em Python. | Alta | Alto | Priorizar painel mínimo em ferramenta existente; programar somente a extensão viável. | Ambos. |
| Comparações interpretadas como ranking de eficiência. | Média | Alto | Mostrar definições e contexto; discutir diferenças assistenciais e limites. | Gabriel. |
| Ausência de avaliadores da gestão hospitalar. | Alta | Médio | Realizar verificação acadêmica e declarar que a utilidade com gestores não foi testada. | Ambos. |
| Referências inexatas ou uso inadequado de IA. | Média | Alto | Conferir fontes, revisar substancialmente o texto e declarar o uso efetivo de ferramentas. | Ambos. |

## 14. Organização da equipe

| Integrante | Papel principal | Responsabilidades | Apoio necessário |
|---|---|---|---|
| Gabriel Silva dos Santos | Fundamentação e conferência. | Mapear documentos, verificar definições, conferir consultas e discutir resultados. | Orientação sobre método e interpretação hospitalar. |
| Maurício Rafael Oliveira da Silva | Preparação e visualização. | Organizar base, registrar transformações, montar painel e documentar eventual código. | Revisão dos indicadores e acesso à ferramenta escolhida. |
| Ambos os autores | Análise e autoria. | Interpretar resultados, revisar o texto, preparar apresentação e assumir responsabilidade acadêmica. | Revisão da orientadora e retorno sobre o escopo. |
| Professora orientadora | Acompanhamento acadêmico. | Avaliar coerência, delimitação e adequação às exigências do curso. | Versões com dados e resultados verificáveis para revisão. |

## 15. Validação da definição do projeto

Itens de definição documental:

- [x] O problema está delimitado e possui fundamentação documental.
- [x] O público-alvo e as partes interessadas estão identificados.
- [x] O objetivo geral e os objetivos específicos são coerentes.
- [x] As perguntas de negócio orientam ações de análise concretas.
- [x] Há fontes públicas potencialmente disponíveis para responder às perguntas.
- [x] Os critérios de sucesso são mensuráveis.
- [x] Riscos, privacidade, ética e uso de IA foram considerados.
- [x] Funções e responsabilidades iniciais foram propostas.

Verificações de execução e aprovação:

- [ ] A coleta confirmou o recorte e a compatibilidade das fontes.
- [ ] O núcleo mínimo mostrou-se executável no prazo.
- [ ] Os autores revisaram substantivamente o conteúdo e conferiram as referências.
- [ ] A orientadora validou o enquadramento e o escopo.

## 16. Aprovação e registro de ajustes

| Responsável | Validação / observação | Data |
|---|---|---|
| Gabriel Silva dos Santos | Espaço para registro após revisão. | A preencher. |
| Maurício Rafael Oliveira da Silva | Espaço para registro após revisão. | A preencher. |
| Professora orientadora | Espaço para validação do escopo, método e modalidade. | A preencher. |

### Ajustes solicitados após a apresentação inicial

| Data | Ajuste solicitado | Responsável | Situação |
|---|---|---|---|
| A preencher. | Registrar ajustes deliberados na reunião. | A definir. | A registrar. |

### Adequação à eventual submissão aos Cadernos do UDF

Este documento define o projeto. O manuscrito científico resultante deverá seguir o Anexo B e o modelo institucional do Edital nº 30/2026, com resultados efetivamente obtidos [18]. Para a modalidade artigo científico, o edital prevê até 25 páginas, resumo de até 250 palavras e três a cinco palavras-chave; exige título e resumo em português e inglês, além das seções científicas e referências. A formatação indicada inclui Times New Roman 12, espaçamento 1,5 e margens superior/esquerda de 3 cm e inferior/direita de 2 cm.

A preparação da submissão também envolve arquivos nos formatos exigidos pelo edital e declarações de originalidade e de uso de IA assinadas pelos autores. A escolha da revista e o atendimento às exigências específicas do TCC serão confirmados com a orientação. A existência desta definição não equivale à aprovação institucional nem à conclusão da pesquisa.

## Referências e documentos de consulta

Os números entre colchetes identificam as fontes utilizadas nas seções. Os endereços abaixo permitem consultar diretamente a documentação. Acesso às fontes on-line: 21 set. 2026.

**[1] SALDANHA, Raphael de Freitas; BASTOS, Ronaldo Rocha; BARCELLOS, Christovam.** Microdatasus: pacote para download e pré-processamento de microdados do Departamento de Informática do SUS (DATASUS). *Cadernos de Saúde Pública*, v. 35, n. 9, e00032419, 2019. DOI: 10.1590/0102-311X00032419. Disponível em: <https://doi.org/10.1590/0102-311X00032419>. Registro do autor: <https://rfsaldanha.github.io/publications/saldanhaMicrodatasusPacotePara2019.html>.

**[2] BRASIL. Ministério da Saúde. DATASUS.** Internações hospitalares do SUS por local de internação: notas técnicas. Disponível em: <https://tabnet.datasus.gov.br/cgi/sih/rxdescr.htm>. Portal de consulta SIH/SUS: <https://datasus.saude.gov.br/acesso-a-informacao/morbidade-hospitalar-do-sus-sih-sus/>. Consultar especialmente as definições de processamento, internações, dias e média de permanência.

**[3] BRASIL. Ministério da Saúde. CNES.** Principais conceitos. Disponível em: <https://wiki.saude.gov.br/cnes/index.php/Principais_Conceitos>. Acesso aos recursos físicos: <https://datasus.saude.gov.br/cnes-recursos-fisicos/>. Consultar as distinções entre leitos existentes, SUS e complementares.

**[4] DISTRITO FEDERAL. Secretaria de Estado de Saúde.** Painel InfoSaúde - Leitos Cadastrados. Disponível em: <https://info.saude.df.gov.br/sala-de-situacao/painel-infosaude-leitos-cadastrados/>.

**[5] DISTRITO FEDERAL. Secretaria de Estado de Saúde.** Painel InfoSaúde - Produção de Serviços: Procedimento Principal. Disponível em: <https://info.saude.df.gov.br/sala-de-situacao/painel-infosaude-producao-de-servicos-procedimento-principal/>.

**[6] RABIEI, Reza; ALMASI, Sohrab.** Requirements and challenges of hospital dashboards: a systematic literature review. *BMC Medical Informatics and Decision Making*, v. 22, art. 287, 2022. DOI: 10.1186/s12911-022-02037-8. Disponível em: <https://doi.org/10.1186/s12911-022-02037-8>.

**[7] BRASIL. Ministério da Saúde.** Sala de Apoio à Gestão Estratégica - SAGE. Disponível em: <https://www.gov.br/saude/pt-br/composicao/seidigi/demas/sage>.

**[8] CONSELHO NACIONAL DE SECRETÁRIOS DE SAÚDE - CONASS.** Conass lança plataforma CNES 360 com dados de estabelecimentos de saúde de todo o Brasil. 14 ago. 2025. Disponível em: <https://www.conass.org.br/conass-lanca-plataforma-cnes-360-com-dados-de-estabelecimentos-de-saude-de-todo-o-brasil/>.

**[9] BRASIL. Secretaria de Governo Digital.** Instrução Normativa SGD/ME nº 94, de 23 de dezembro de 2022. Processo de contratação de soluções de TIC. Texto disponibilizado no portal Governo Digital. Disponível em: <https://www.gov.br/governodigital/pt-br/contratacoes-de-tic/legislacao/processo-de-contratacao-de-solucoes-de-tic-regido-pela-lei-ndeg-14-133-de-2021>. Consultar âmbito de aplicação, planejamento e termo de referência.

**[10] LEBON RÉGIS (SC). Prefeitura Municipal.** Termo de referência: software de saúde. 2025. Disponível em: <https://lebonregis.sc.gov.br/uploads/sites/446/2025/07/TR_SOFTWARE_SAUDE_assinado.pdf>. Localização: recursos de BI e relatórios, aproximadamente p. 68 e 73-75; implantação e capacitação, aproximadamente p. 97, segundo a paginação do arquivo PDF.

**[11] MICROSOFT.** O que é o Power BI? Documentação Microsoft Learn. Disponível em: <https://learn.microsoft.com/pt-br/power-bi/fundamentals/power-bi-overview>.

**[12] TABLEAU.** Healthcare and life sciences analytics. Disponível em: <https://www.tableau.com/solutions/industries/healthcare-life-sciences>.

**[13] QLIK.** Healthcare analytics. Disponível em: <https://www.qlik.com/us/solutions/industries/healthcare-analytics>.

**[14] APACHE SOFTWARE FOUNDATION.** Apache Superset. Disponível em: <https://superset.apache.org/>.

**[15] STREAMLIT.** Streamlit documentation. Disponível em: <https://docs.streamlit.io/>.

**[16] PLOTLY.** Plotly Python Open Source Graphing Library. Disponível em: <https://plotly.com/python/>.

**[17] CONSELHO NACIONAL DE DESENVOLVIMENTO CIENTÍFICO E TECNOLÓGICO - CNPq.** Tabela de áreas do conhecimento. Disponível em: <https://lattes.cnpq.br/documents/11871/24930/TabeladeAreasdoConhecimento.pdf/d192ff6b-3e0a-4074-a74d-c280521bd5f7>. Consultar Ciências da Computação, Metodologia e Técnicas da Computação e Sistemas de Informação.

**[18] CENTRO UNIVERSITÁRIO DO DISTRITO FEDERAL - UDF.** Edital nº 30/2026 - Reitoria: chamada para submissão de trabalhos nas revistas científicas “Cadernos do UDF” 2026. Brasília, 8 set. 2026. Consultar itens 3.2-3.4 e 4.2, Anexo B e Anexo D. Documento institucional; endereço público não identificado nesta consulta.

**[19] CENTRO UNIVERSITÁRIO DO DISTRITO FEDERAL - UDF.** Retificação do Edital nº 30/2026 - Reitoria. Brasília, 9 set. 2026. Corrige o Anexo A e indica encerramento das submissões em 28 set. 2026. Documento institucional; endereço público não identificado nesta consulta.
