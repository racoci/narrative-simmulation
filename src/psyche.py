"""
Módulo que implementa o personagem (Psyche Module).
"""

from typing import Dict, List, Any, Optional, Set, Union
from src.hypergraph import Hypergraph
from src.nodes import PersonalityNode, ValueNode, NeedNode, HabitNode, BeliefNode
from src.edges import MemoryEdge, EmotionEdge, RuleEdge


class PsycheModule:
    """
    Classe que implementa o módulo de personagem (Psyche Module).
    Encapsula o estado interno completo de um personagem.
    """
    
    def __init__(self, character_id: str, name: str):
        """
        Inicializa o módulo de personagem.
        
        Args:
            character_id: ID único do personagem.
            name: Nome do personagem.
        """
        self.character_id = character_id
        self.name = name
        self.psyche = Hypergraph(graph_id=f"psyche_{character_id}", name=f"Psyche of {name}")
        self.current_time = 0
        
    def add_personality_trait(self, trait: str, value: float) -> PersonalityNode:
        """
        Adiciona um traço de personalidade ao personagem.
        
        Args:
            trait: Nome do traço de personalidade.
            value: Valor do traço (entre 0 e 1).
            
        Returns:
            O nó de personalidade criado.
        """
        node = PersonalityNode(trait=trait, value=value)
        self.psyche.add_node(node)
        return node
    
    def add_value(self, value_name: str, priority: float) -> ValueNode:
        """
        Adiciona um valor ao personagem.
        
        Args:
            value_name: Nome do valor.
            priority: Prioridade do valor (entre 0 e 1).
            
        Returns:
            O nó de valor criado.
        """
        node = ValueNode(value_name=value_name, priority=priority)
        self.psyche.add_node(node)
        return node
    
    def add_need(self, need_name: str, satisfaction: float) -> NeedNode:
        """
        Adiciona uma necessidade ao personagem.
        
        Args:
            need_name: Nome da necessidade.
            satisfaction: Nível de satisfação da necessidade (entre 0 e 1).
            
        Returns:
            O nó de necessidade criado.
        """
        node = NeedNode(need_name=need_name, satisfaction=satisfaction)
        self.psyche.add_node(node)
        return node
    
    def add_habit(self, habit_name: str, strength: float) -> HabitNode:
        """
        Adiciona um hábito ao personagem.
        
        Args:
            habit_name: Nome do hábito.
            strength: Força do hábito (entre 0 e 1).
            
        Returns:
            O nó de hábito criado.
        """
        node = HabitNode(habit_name=habit_name, strength=strength)
        self.psyche.add_node(node)
        return node
    
    def add_belief(self, content: str, confidence: float) -> BeliefNode:
        """
        Adiciona uma crença ao personagem.
        
        Args:
            content: Conteúdo da crença.
            confidence: Nível de confiança na crença (entre 0 e 1).
            
        Returns:
            O nó de crença criado.
        """
        node = BeliefNode(content=content, confidence=confidence)
        self.psyche.add_node(node)
        return node
    
    def add_memory(self, nodes: List[str], emotion_tag: str, intensity: float, 
                   salience: float, is_cornerstone: bool = False, 
                   description: str = "") -> MemoryEdge:
        """
        Adiciona uma memória ao personagem.
        
        Args:
            nodes: Lista de IDs dos nós conectados pela memória.
            emotion_tag: Tag emocional associada à memória.
            intensity: Intensidade da emoção (entre 0 e 1).
            salience: Saliência da memória (entre 0 e 1).
            is_cornerstone: Indica se esta é uma memória fundamental (cornerstone).
            description: Descrição textual do evento.
            
        Returns:
            A hiper-aresta de memória criada.
        """
        edge = MemoryEdge(
            nodes=nodes,
            emotion_tag=emotion_tag,
            intensity=intensity,
            salience=salience,
            is_cornerstone=is_cornerstone,
            timestamp=self.current_time,
            description=description
        )
        self.psyche.add_edge(edge)
        return edge
    
    def add_emotion(self, nodes: List[str], emotion: str, target: Optional[str] = None,
                    intensity: float = 0.5, decay_rate: float = 0.1) -> EmotionEdge:
        """
        Adiciona uma emoção ao personagem.
        
        Args:
            nodes: Lista de IDs dos nós conectados pela emoção.
            emotion: Nome da emoção.
            target: ID do alvo da emoção (opcional).
            intensity: Intensidade da emoção (entre 0 e 1).
            decay_rate: Taxa de decaimento da emoção ao longo do tempo.
            
        Returns:
            A hiper-aresta de emoção criada.
        """
        edge = EmotionEdge(
            nodes=nodes,
            emotion=emotion,
            target=target,
            intensity=intensity,
            decay_rate=decay_rate,
            timestamp=self.current_time
        )
        self.psyche.add_edge(edge)
        return edge
    
    def add_rule(self, nodes: List[str], trigger: str, action: str, 
                 confidence: float = 0.5) -> RuleEdge:
        """
        Adiciona uma regra ao personagem.
        
        Args:
            nodes: Lista de IDs dos nós conectados pela regra.
            trigger: Condição que ativa a regra.
            action: Ação a ser executada quando a regra é ativada.
            confidence: Nível de confiança na regra (entre 0 e 1).
            
        Returns:
            A hiper-aresta de regra criada.
        """
        edge = RuleEdge(
            nodes=nodes,
            trigger=trigger,
            action=action,
            confidence=confidence
        )
        self.psyche.add_edge(edge)
        return edge
    
    def get_personality_traits(self) -> List[PersonalityNode]:
        """
        Obtém todos os traços de personalidade do personagem.
        
        Returns:
            Lista de nós de personalidade.
        """
        return [node for node in self.psyche.nodes.values() 
                if isinstance(node, PersonalityNode)]
    
    def get_values(self) -> List[ValueNode]:
        """
        Obtém todos os valores do personagem.
        
        Returns:
            Lista de nós de valor.
        """
        return [node for node in self.psyche.nodes.values() 
                if isinstance(node, ValueNode)]
    
    def get_needs(self) -> List[NeedNode]:
        """
        Obtém todas as necessidades do personagem.
        
        Returns:
            Lista de nós de necessidade.
        """
        return [node for node in self.psyche.nodes.values() 
                if isinstance(node, NeedNode)]
    
    def get_habits(self) -> List[HabitNode]:
        """
        Obtém todos os hábitos do personagem.
        
        Returns:
            Lista de nós de hábito.
        """
        return [node for node in self.psyche.nodes.values() 
                if isinstance(node, HabitNode)]
    
    def get_beliefs(self) -> List[BeliefNode]:
        """
        Obtém todas as crenças do personagem.
        
        Returns:
            Lista de nós de crença.
        """
        return [node for node in self.psyche.nodes.values() 
                if isinstance(node, BeliefNode)]
    
    def get_memories(self) -> List[MemoryEdge]:
        """
        Obtém todas as memórias do personagem.
        
        Returns:
            Lista de hiper-arestas de memória.
        """
        return [edge for edge in self.psyche.edges.values() 
                if isinstance(edge, MemoryEdge)]
    
    def get_emotions(self) -> List[EmotionEdge]:
        """
        Obtém todas as emoções do personagem.
        
        Returns:
            Lista de hiper-arestas de emoção.
        """
        return [edge for edge in self.psyche.edges.values() 
                if isinstance(edge, EmotionEdge)]
    
    def get_rules(self) -> List[RuleEdge]:
        """
        Obtém todas as regras do personagem.
        
        Returns:
            Lista de hiper-arestas de regra.
        """
        return [edge for edge in self.psyche.edges.values() 
                if isinstance(edge, RuleEdge)]
    
    def get_cornerstone_memories(self) -> List[MemoryEdge]:
        """
        Obtém todas as memórias fundamentais (cornerstone) do personagem.
        
        Returns:
            Lista de hiper-arestas de memória fundamentais.
        """
        return [edge for edge in self.get_memories() 
                if edge.is_cornerstone]
    
    def get_current_emotions(self) -> List[EmotionEdge]:
        """
        Obtém as emoções atuais do personagem (com intensidade significativa).
        
        Returns:
            Lista de hiper-arestas de emoção atuais.
        """
        return [edge for edge in self.get_emotions() 
                if edge.intensity > 0.1]  # Limiar arbitrário
    
    def update(self, current_time: int) -> None:
        """
        Atualiza o estado interno do personagem.
        
        Args:
            current_time: Tempo atual da simulação.
        """
        self.current_time = current_time
        
        # Atualiza a intensidade das emoções com base no tempo decorrido
        for emotion in self.get_emotions():
            emotion.update_intensity(current_time)
            
    def create_from_archetype(self, archetype: Dict[str, Any]) -> None:
        """
        Cria um personagem a partir de um arquétipo.
        
        Args:
            archetype: Dicionário descrevendo o arquétipo do personagem.
        """
        # Adiciona traços de personalidade
        for trait, value in archetype.get("personality", {}).items():
            self.add_personality_trait(trait, value)
            
        # Adiciona valores
        for value_name, priority in archetype.get("values", {}).items():
            self.add_value(value_name, priority)
            
        # Adiciona necessidades
        for need_name, satisfaction in archetype.get("needs", {}).items():
            self.add_need(need_name, satisfaction)
            
        # Adiciona hábitos
        for habit_name, strength in archetype.get("habits", {}).items():
            self.add_habit(habit_name, strength)
            
        # Adiciona crenças
        for belief in archetype.get("beliefs", []):
            self.add_belief(belief["content"], belief["confidence"])
            
    def save_to_file(self, filepath: str) -> None:
        """
        Salva o estado do personagem em um arquivo.
        
        Args:
            filepath: Caminho do arquivo onde o estado será salvo.
        """
        self.psyche.save_to_file(filepath)
        
    @classmethod
    def load_from_file(cls, filepath: str, character_id: str, name: str) -> 'PsycheModule':
        """
        Carrega o estado de um personagem de um arquivo.
        
        Args:
            filepath: Caminho do arquivo de onde o estado será carregado.
            character_id: ID único do personagem.
            name: Nome do personagem.
            
        Returns:
            Uma instância de PsycheModule.
        """
        psyche_module = cls(character_id=character_id, name=name)
        psyche_module.psyche = Hypergraph.load_from_file(filepath)
        return psyche_module

