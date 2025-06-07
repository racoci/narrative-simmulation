"""
Módulo que implementa os tipos específicos de hiper-arestas para o hiper-grafo de personagem.
"""

from typing import Dict, List, Any, Optional, Union
from src.hypergraph import Hyperedge


class MemoryEdge(Hyperedge):
    """
    Representa uma memória que conecta nós que participaram de um evento.
    Implementação das "Cornerstone Memories".
    """
    
    def __init__(self, edge_id: Optional[str] = None, nodes: Optional[List[str]] = None,
                 emotion_tag: str = "", intensity: float = 0.5, salience: float = 0.5,
                 is_cornerstone: bool = False, timestamp: Optional[int] = None,
                 description: str = ""):
        """
        Inicializa uma hiper-aresta de memória.
        
        Args:
            edge_id: ID único da hiper-aresta. Se não fornecido, um UUID será gerado.
            nodes: Lista de IDs dos nós conectados por esta hiper-aresta.
            emotion_tag: Tag emocional associada à memória (ex: "Fear", "Joy").
            intensity: Intensidade da emoção (entre 0 e 1).
            salience: Saliência da memória (entre 0 e 1).
            is_cornerstone: Indica se esta é uma memória fundamental (cornerstone).
            timestamp: Timestamp do evento (opcional).
            description: Descrição textual do evento.
        """
        super().__init__(edge_id=edge_id, edge_type="Memory", nodes=nodes)
        self.emotion_tag = emotion_tag
        self.intensity = max(0.0, min(1.0, intensity))  # Garante que a intensidade esteja entre 0 e 1
        self.salience = max(0.0, min(1.0, salience))  # Garante que a saliência esteja entre 0 e 1
        self.is_cornerstone = is_cornerstone
        self.timestamp = timestamp
        self.description = description
        
    def to_dict(self) -> Dict[str, Any]:
        """
        Converte a hiper-aresta para um dicionário.
        
        Returns:
            Um dicionário representando a hiper-aresta.
        """
        data = super().to_dict()
        data.update({
            "emotion_tag": self.emotion_tag,
            "intensity": self.intensity,
            "salience": self.salience,
            "is_cornerstone": self.is_cornerstone,
            "timestamp": self.timestamp,
            "description": self.description
        })
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'MemoryEdge':
        """
        Cria uma hiper-aresta de memória a partir de um dicionário.
        
        Args:
            data: Dicionário contendo os dados da hiper-aresta.
            
        Returns:
            Uma instância de MemoryEdge.
        """
        return cls(
            edge_id=data.get("id"),
            nodes=data.get("nodes", []),
            emotion_tag=data.get("emotion_tag", ""),
            intensity=data.get("intensity", 0.5),
            salience=data.get("salience", 0.5),
            is_cornerstone=data.get("is_cornerstone", False),
            timestamp=data.get("timestamp"),
            description=data.get("description", "")
        )
    
    def __str__(self) -> str:
        cornerstone = " (Cornerstone)" if self.is_cornerstone else ""
        return f"MemoryEdge(id={self.id}, emotion={self.emotion_tag}, intensity={self.intensity:.2f}{cornerstone})"


class EmotionEdge(Hyperedge):
    """
    Representa um estado emocional atual, conectando a causa da emoção aos valores e necessidades afetados.
    """
    
    def __init__(self, edge_id: Optional[str] = None, nodes: Optional[List[str]] = None,
                 emotion: str = "", target: Optional[str] = None, decay_rate: float = 0.1,
                 intensity: float = 0.5, timestamp: Optional[int] = None):
        """
        Inicializa uma hiper-aresta de emoção.
        
        Args:
            edge_id: ID único da hiper-aresta. Se não fornecido, um UUID será gerado.
            nodes: Lista de IDs dos nós conectados por esta hiper-aresta.
            emotion: Nome da emoção (ex: "Anger", "Joy").
            target: ID do alvo da emoção (opcional).
            decay_rate: Taxa de decaimento da emoção ao longo do tempo.
            intensity: Intensidade da emoção (entre 0 e 1).
            timestamp: Timestamp de quando a emoção foi criada (opcional).
        """
        super().__init__(edge_id=edge_id, edge_type="Emotion", nodes=nodes)
        self.emotion = emotion
        self.target = target
        self.decay_rate = max(0.0, min(1.0, decay_rate))  # Garante que a taxa de decaimento esteja entre 0 e 1
        self.intensity = max(0.0, min(1.0, intensity))  # Garante que a intensidade esteja entre 0 e 1
        self.timestamp = timestamp
        
    def update_intensity(self, current_time: int) -> None:
        """
        Atualiza a intensidade da emoção com base no tempo decorrido.
        
        Args:
            current_time: Timestamp atual.
        """
        if self.timestamp is not None:
            time_elapsed = current_time - self.timestamp
            self.intensity *= (1 - self.decay_rate) ** time_elapsed
            self.timestamp = current_time
        
    def to_dict(self) -> Dict[str, Any]:
        """
        Converte a hiper-aresta para um dicionário.
        
        Returns:
            Um dicionário representando a hiper-aresta.
        """
        data = super().to_dict()
        data.update({
            "emotion": self.emotion,
            "target": self.target,
            "decay_rate": self.decay_rate,
            "intensity": self.intensity,
            "timestamp": self.timestamp
        })
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'EmotionEdge':
        """
        Cria uma hiper-aresta de emoção a partir de um dicionário.
        
        Args:
            data: Dicionário contendo os dados da hiper-aresta.
            
        Returns:
            Uma instância de EmotionEdge.
        """
        return cls(
            edge_id=data.get("id"),
            nodes=data.get("nodes", []),
            emotion=data.get("emotion", ""),
            target=data.get("target"),
            decay_rate=data.get("decay_rate", 0.1),
            intensity=data.get("intensity", 0.5),
            timestamp=data.get("timestamp")
        )
    
    def __str__(self) -> str:
        target_str = f", target={self.target}" if self.target else ""
        return f"EmotionEdge(id={self.id}, emotion={self.emotion}, intensity={self.intensity:.2f}{target_str})"


class RuleEdge(Hyperedge):
    """
    Representa uma regra de reescrita do próprio hiper-grafo, a base da aprendizagem e da "transvaloração".
    """
    
    def __init__(self, edge_id: Optional[str] = None, nodes: Optional[List[str]] = None,
                 trigger: str = "", action: str = "", confidence: float = 0.5):
        """
        Inicializa uma hiper-aresta de regra.
        
        Args:
            edge_id: ID único da hiper-aresta. Se não fornecido, um UUID será gerado.
            nodes: Lista de IDs dos nós conectados por esta hiper-aresta.
            trigger: Condição que ativa a regra.
            action: Ação a ser executada quando a regra é ativada.
            confidence: Nível de confiança na regra (entre 0 e 1).
        """
        super().__init__(edge_id=edge_id, edge_type="Rule", nodes=nodes)
        self.trigger = trigger
        self.action = action
        self.confidence = max(0.0, min(1.0, confidence))  # Garante que a confiança esteja entre 0 e 1
        
    def to_dict(self) -> Dict[str, Any]:
        """
        Converte a hiper-aresta para um dicionário.
        
        Returns:
            Um dicionário representando a hiper-aresta.
        """
        data = super().to_dict()
        data.update({
            "trigger": self.trigger,
            "action": self.action,
            "confidence": self.confidence
        })
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'RuleEdge':
        """
        Cria uma hiper-aresta de regra a partir de um dicionário.
        
        Args:
            data: Dicionário contendo os dados da hiper-aresta.
            
        Returns:
            Uma instância de RuleEdge.
        """
        return cls(
            edge_id=data.get("id"),
            nodes=data.get("nodes", []),
            trigger=data.get("trigger", ""),
            action=data.get("action", ""),
            confidence=data.get("confidence", 0.5)
        )
    
    def __str__(self) -> str:
        return f"RuleEdge(id={self.id}, confidence={self.confidence:.2f})"

