# Sistema Unificado de Simulação de Personagens, Relacionamentos e Narrativas Complexas

A seguir, apresento uma proposta detalhada de implementação para o **Sistema Unificado de Simulação de Personagens, Relacionamentos e Narrativas Complexas**. Esta proposta transforma o esboço algorítmico em um plano de trabalho concreto, detalhando a arquitetura de software, as estruturas de dados, as tarefas de implementação e uma interface de visualização para análise e depuração.

### **Proposta de Implementação: Sistema de Narrativa Emergente (SNE)**

#### **1. Visão Geral e Filosofia de Design**

O objetivo é construir um sistema de software, o SNE, que não gere histórias, mas sim **simule "vidas digitais"**. A narrativa é um resultado emergente das interações entre agentes psicologicamente profundos em um mundo simulado. A filosofia de design é modular, baseada em agentes e altamente extensível, permitindo que diferentes modelos teóricos (psicológicos, filosóficos, narrativos) possam ser conectados ou trocados.

A arquitetura central se baseia em um **Núcleo de Simulação** que gerencia o tempo e a atualização dos estados, e um conjunto de **Agentes de Personagem (NPCs)** que operam de forma autônoma dentro dele.

#### **2. Arquitetura do Sistema**

O SNE será estruturado em cinco módulos principais que interagem entre si:

1.  **Módulo de Mundo (World Module):**
    * **Responsabilidade:** Gerencia o estado do ambiente de simulação. Contém objetos, locais e o estado físico do mundo. Serve como a "verdade fundamental" que os personagens percebem.
    * **Implementação:** Uma estrutura de dados de cena (Scene Graph) ou uma simples base de dados de entidades e seus estados (posição, propriedades). Fornece uma API para que os agentes possam perceber (`perceive(area)`) e agir (`act(action)`).

2.  **Módulo de Personagem (Psyche Module):**
    * **Responsabilidade:** O coração de cada NPC. Encapsula o estado interno completo de um personagem. É uma instância única para cada agente.
    * **Implementação:** Contém a estrutura de dados principal: o **Hiper-grafo de Personagem (`P_NPC`)**. Gerencia as atualizações de baixo nível neste grafo (adicionar memória, fortalecer hábito) conforme instruído pelo Módulo de Cognição.

3.  **Módulo de Cognição (Cognition Module):**
    * **Responsabilidade:** O "processador" do personagem. Executa o ciclo de decisão do agente. É aqui que as teorias são transformadas em lógica computacional.
    * **Implementação:** Contém a implementação do **Ciclo do Ato Humano Expandido**. Interage com todos os outros módulos:
        * Lê do `Módulo de Mundo` (Percepção).
        * Lê do `Módulo de Personagem` (acessa memórias, valores, personalidade).
        * Usa o `Módulo de Relacionamento` para avaliar ações sociais.
        * Envia a ação escolhida de volta ao `Módulo de Mundo`.
        * Instrui o `Módulo de Personagem` sobre quais atualizações fazer no hiper-grafo (aprendizagem).

4.  **Módulo de Relacionamento (Relationship Module):**
    * **Responsabilidade:** Modela a dinâmica entre dois ou mais personagens.
    * **Implementação:** Gerencia um conjunto de **Hiper-grafos de Relacionamento (`R_AB`)**. Contém a lógica da Teoria da Troca Social (SET) para calcular custos/benefícios e o modelo de estágios de Knapp para categorizar o estado do relacionamento.

5.  **Módulo Narrativo (Narrative Director):**
    * **Responsabilidade:** Atua como um "mestre de jogo" ou diretor de IA. Define objetivos de alto nível, introduz eventos externos (gatilhos de história) e aplica restrições para guiar a narrativa sem microgerenciar os agentes.
    * **Implementação:** Utiliza um planejador **HTN (Hierarchical Task Network)**. Os "loops" dos anfitriões de Westworld são tarefas de alto nível no HTN. O diretor pode atribuir novas tarefas de alto nível aos agentes (por exemplo, "Investigar o mistério da caverna") que seus Módulos de Cognição tentarão resolver.

#### **3. Estruturas de Dados Chave: O Hiper-grafo de Personagem (`P_NPC`)**

O hiper-grafo é a estrutura de dados central que representa a psique de um personagem. Ele é composto por Nós (conceitos) e Hiper-arestas (relações complexas entre conceitos).

* **Nós (Nodes):**
    * **`PersonalityNode`**: Representa um traço FFM/HEXACO. Ex: `{ id: 'p01', type: 'Personality', trait: 'HonestyHumility', value: 0.8 }`.
    * **`ValueNode`**: Representa um valor do modelo de Schwartz/Scheler. Ex: `{ id: 'v01', type: 'Value', valueName: 'Security', priority: 0.95 }`.
    * **`NeedNode`**: Representa uma necessidade (Maslow/Bens Básicos). Ex: `{ id: 'n01', type: 'Need', needName: 'Belonging', satisfaction: 0.3 }`.
    * **`HabitNode`**: Representa uma virtude ou vício. Ex: `{ id: 'h01', type: 'Habit', habitName: 'Courage', strength: 0.7 }`.
    * **`BeliefNode`**: Uma crença formada sobre o mundo ou sobre si mesmo. Ex: `{ id: 'b01', type: 'Belief', content: 'O mundo é perigoso', confidence: 0.88 }`.

* **Hiper-arestas (Hyperedges):**
    * **`MemoryEdge`**: Conecta nós que participaram de um evento. Esta é a implementação das "Cornerstone Memories". Ex: `{ id: 'm01', type: 'Memory', nodes: [event_id, self_id, other_char_id], emotionTag: 'Fear', intensity: 0.9, salience: 0.98, isCornerstone: true }`.
    * **`EmotionEdge`**: Representa um estado emocional atual, conectando a causa da emoção (um `MemoryEdge`) aos `ValueNode`s e `NeedNode`s que a emoção afeta. Ex: `{ id: 'e01', type: 'Emotion', emotion: 'Anger', target: 'other_char_id', decayRate: 0.1 }`.
    * **`RuleEdge`**: Representa uma regra de reescrita do próprio hiper-grafo, a base da aprendizagem e da "transvaloração". Ex: `{ id: 'r01', type: 'RewriteRule', trigger: '[MemoryEdge(type=Betrayal), ValueNode(valueName=Benevolence, priority>0.8)]', action: 'decrease_priority(ValueNode:Benevolence, 0.2); increase_priority(ValueNode:Security, 0.3)' }`.

#### **4. Plano de Implementação por Tarefas**

**Fase 1: Fundações e Estruturas de Dados**
1.  **Definir as Classes:** Criar as classes base em Python (ou outra linguagem) para `Node`, `Hyperedge`, e o próprio `Hypergraph`.
2.  **Implementar o Núcleo de Simulação:** Desenvolver o loop de tempo principal (`tick`) e o registro de agentes.
3.  **Criar o Módulo de Mundo Básico:** Implementar um sistema simples de entidades e posições.

**Fase 2: O Agente Básico (Personalidade e Cognição)**
1.  **Construir o Módulo de Personagem:** Implementar a capacidade de criar um `P_NPC` com base em um arquétipo (valores iniciais de personalidade, valores, etc.).
2.  **Implementar o Módulo de Cognição (Ato Humano):**
    * Mapear as 12 etapas do Ato Humano para funções de software.
    * Integrar o modelo OCC para a geração de `EmotionEdge`s a partir de eventos.
    * Criar um mecanismo de seleção de ação básico que considera o estado emocional e os traços de personalidade.
3.  **Implementar o Módulo de Aprendizagem:** Desenvolver o sistema de reescrita de hiper-grafos para que as ações atualizem o `P_NPC` (formação de memórias e hábitos).

**Fase 3: O Agente Social (Relacionamentos)**
1.  **Criar o Módulo de Relacionamento:** Implementar a estrutura `R_AB`.
2.  **Desenvolver o Avaliador de Troca Social (SET):** Criar uma função que avalia uma interação social com base nos recursos de Foa & Foa e atualiza métricas como "confiança" e "dívida" no `R_AB`.
3.  **Refinar o Módulo de Cognição:** Expandir a seleção de ação para incluir considerações sociais (por exemplo, "Ajudar este agente aumentará nossa confiança?").

**Fase 4: O Agente Narrativo (História e Emergência)**
1.  **Integrar o Módulo Narrativo:** Conectar um planejador HTN ao sistema.
2.  **Definir Tarefas e Métodos:** Criar uma biblioteca de "loops" narrativos (tarefas HTN como "Trabalhar na fazenda") e métodos para realizá-los.
3.  **Implementar a "Improvisação":** Criar a lógica no Módulo de Cognição para gerar objetivos de alta prioridade (baseados em emoções fortes ou necessidades críticas) que possam substituir o plano HTN atual.
4.  **Desenvolver o Módulo de Meta-Narrativa:** Implementar o algoritmo de "reflexão" periódica que analisa o `P_NPC` em busca de padrões e gera `BeliefNode`s.

#### **5. Proposta de Visualização: O "Painel da Psique"**

Para depurar, analisar e visualizar o funcionamento interno do SNE, é essencial uma ferramenta de visualização interativa. Proponho um "Painel da Psique", uma aplicação web de página única.

**Layout da Interface:**

* **Painel Esquerdo (Lista de Agentes):** Uma lista de todos os NPCs na simulação. Clicar em um NPC o torna o foco do painel.
* **Painel Central (Visualizador do Hiper-grafo):**
    * Renderiza o `P_NPC` do agente selecionado de forma interativa. Nós são exibidos como círculos/quadrados coloridos e hiper-arestas como linhas ou áreas de conexão.
    * Utilizaria uma técnica como **PAOH (Parallel Aggregated Ordered Hypergraph)** para lidar com a complexidade e a natureza dinâmica do grafo.
    * **Interatividade:**
        * **Zoom e Pan:** Para navegar em grafos grandes.
        * **Filtros:** Para mostrar/ocultar tipos de nós ou arestas (ex: "mostrar apenas Memórias e Valores").
        * **Clique em Nós/Arestas:** Selecionar um elemento exibe seus dados brutos e descrição no Painel de Contexto.
* **Painel Direito (Painel de Contexto):**
    * Exibe os detalhes do nó ou aresta selecionado.
    * Se um `ValueNode` for selecionado, mostra seu nome e prioridade.
    * Se uma `MemoryEdge` for selecionada, mostra a descrição do evento, a emoção associada e sua intensidade.
    * Permite a edição manual de valores para fins de teste.
* **Painel Inferior (Log de Decisão e Linha do Tempo):**
    * **Aba 1: Log de Decisão em Tempo Real:** Mostra as etapas do "Ato Humano" para a decisão mais recente do agente. Destaca quais `ValueNode`s, `EmotionEdge`s e `MemoryEdge`s foram mais influentes. Essencial para entender por que uma "improvisação" ocorreu.
    * **Aba 2: Linha do Tempo de Vida:** Exibe os eventos mais significativos (especialmente `Cornerstone Memories`) na vida do agente em uma linha do tempo, permitindo ver como a personalidade e os valores mudaram após cada evento.

Esta proposta fornece um roteiro abrangente para transformar o conceito teórico em um sistema de software funcional e analisável, com um caminho claro desde as estruturas de dados fundamentais até a visualização de comportamentos emergentes complexos.
