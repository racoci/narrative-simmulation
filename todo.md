# Progresso do Projeto

## Fase 1: Fundações e Estruturas de Dados
- [x] Definir as Classes: Criar as classes base em Python (ou outra linguagem) para `Node`, `Hyperedge`, e o próprio `Hypergraph`.
- [x] Implementar o Núcleo de Simulação: Desenvolver o loop de tempo principal (`tick`) e o registro de agentes.
- [x] Criar o Módulo de Mundo Básico: Implementar um sistema simples de entidades e posições.

## Fase 2: O Agente Básico (Personalidade e Cognição)
- [x] Construir o Módulo de Personagem: Implementar a capacidade de criar um `P_NPC` com base em um arquétipo (valores iniciais de personalidade, valores, etc.).
- [ ] Implementar o Módulo de Cognição (Ato Humano):
    - [x] Mapear as 12 etapas do Ato Humano para funções de software.
    - [x] Integrar o modelo OCC para a geração de `EmotionEdge`s a partir de eventos.
    - [x] Criar um mecanismo de seleção de ação básico que considera o estado emocional e os traços de personalidade.
- [x] Implementar o Módulo de Aprendizagem: Desenvolver o sistema de reescrita de hiper-grafos para que as ações atualizem o `P_NPC` (formação de memórias e hábitos).

## Fase 3: O Agente Social (Relacionamentos)
- [ ] Criar o Módulo de Relacionamento: Implementar a estrutura `R_AB`.
- [ ] Desenvolver o Avaliador de Troca Social (SET): Criar uma função que avalia uma interação social com base nos recursos de Foa & Foa e atualiza métricas como "confiança" e "dívida" no `R_AB`.
- [ ] Refinar o Módulo de Cognição: Expandir a seleção de ação para incluir considerações sociais (por exemplo, "Ajudar este agente aumentará nossa confiança?").

## Fase 4: O Agente Narrativo (História e Emergência)
- [ ] Integrar o Módulo Narrativo: Conectar um planejador HTN ao sistema.
- [ ] Definir Tarefas e Métodos: Criar uma biblioteca de "loops" narrativos (tarefas HTN como "Trabalhar na fazenda") e métodos para realizá-los.
- [ ] Implementar a "Improvisação": Criar a lógica no Módulo de Cognição para gerar objetivos de alta prioridade (baseados em emoções fortes ou necessidades críticas) que possam substituir o plano HTN atual.
- [ ] Desenvolver o Módulo de Meta-Narrativa: Implementar o algoritmo de "reflexão" periódica que analisa o `P_NPC` em busca de padrões e gera `BeliefNode`s.


