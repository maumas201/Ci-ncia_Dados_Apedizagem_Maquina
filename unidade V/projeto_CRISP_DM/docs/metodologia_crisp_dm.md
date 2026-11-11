# Aplicação do CRISP-DM

O CRISP-DM organiza um processo iterativo: descobertas nos dados podem exigir mudança na pergunta, na preparação ou na análise. Neste projeto, ele orienta uma análise descritiva. Não é empregado como alegação de treinamento de modelo preditivo.

## 1. Entendimento do negócio
**Problema:** informações administrativas sobre produção e estrutura têm unidades de observação distintas. Gráficos feitos sem definir essas unidades podem induzir interpretações erradas.

**Público pretendido:** estudantes e analistas interessados em explorar registros do SUS. Não houve levantamento com usuários nem comprovação de utilidade para gestores.

**Objetivo:** descrever distribuição de registros de AIH, valores e leitos cadastrados por estabelecimento. A entrega não objetiva avaliar qualidade assistencial.

**Critérios de conclusão desta atividade:** código executável; gráficos com unidade, competência e universo; conservação das somas em relação ao piloto; respostas apoiadas nos cálculos; documentação das limitações. Os critérios desta análise foram estabelecidos após a realização do piloto exploratório.

**Recursos e riscos:** Python, pandas, matplotlib, tabela agregada e evidências do piloto. Riscos: interpretação indevida de AIH, perda de zeros à esquerda no CNES, comparação de universos diferentes. As medidas de controle compreendem tipos explícitos, verificações e identificação do universo nos gráficos.

## 2. Entendimento dos dados
Fontes originais: RDDF2506, STDF2506 e LTDF2506. O CSV desta atividade é um resultado agregado do piloto; cada linha representa um CNES em uma competência. Não contém linhas individuais de pacientes. A procedência e os campos estão descritos em `dados/README.md`.

A inspeção verifica tipos, chaves, ausências e valores inválidos nos campos efetivamente usados. A ausência de falhas nessas verificações não certifica qualidade de toda a base original.

## 3. Preparação dos dados
No piloto, RD e LT foram agregados separadamente antes da integração por estabelecimento e competência. A junção direta era inadequada porque podia replicar a produção para múltiplas categorias de leitos. ST forneceu atributos cadastrais.

Nesta atividade, lemos o CSV já agregado; preservamos CNES e competência como texto, verificamos unicidade e somas e ordenamos os estabelecimentos. Não apagamos duplicidades automaticamente, não preenchemos ausências com zero e associamos nomes consultados no CNES pelo código, com verificação de cardinalidade um para um. Centavos são preservados como inteiros nos cálculos monetários; a conversão para reais é feita na apresentação.

## 4. Modelagem — adaptação descritiva
As técnicas empregadas são contagem, soma, participação percentual, ordenação e visualização. Não há variável-alvo, divisão treino/teste ou ajuste de algoritmo preditivo. As barras permitem comparar categorias; a dispersão mostra a distribuição conjunta de duas variáveis numéricas. O corte dos dez maiores torna os rótulos legíveis, sem remover os demais dos totais.

A modelagem analítica organiza medidas e comparações descritivas. Não são empregados algoritmos preditivos ou de agrupamento.

## 5. Avaliação
O script interrompe a geração se alguma verificação obrigatória falhar. Compara contagens, tipos de AIH, valores e leitos com o resumo preservado do piloto, verifica chave única, formato e ausência de valores negativos nos campos utilizados. Os resultados ficam em `resultados/verificacoes.json`.

As verificações são internas e compartilham a origem dos dados de referência. Não substituem conciliação externa com TABNET. Não são estimados efeitos causais nem feitas previsões. O relatório identifica o que os gráficos mostram e o que não permitem concluir.

## 6. Implementação e revisão
A entrega consiste em script, notebook de apoio, agregados, gráficos, documentação e evidências de execução. Publicação no GitHub é uma forma de disponibilizar a análise, não uma implantação hospitalar. 

A reprodução utiliza a tabela agregada, as dependências declaradas e o script versionado. A análise está delimitada à competência de junho de 2025. Uma aplicação a outras competências requer nova extração e revisão da correspondência temporal entre produção e cadastro.
