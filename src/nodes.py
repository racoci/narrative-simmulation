"""
Módulo que implementa os tipos específicos de nós para o hiper-grafo de personagem.
"""

from typing import Dict, List, Any, Optional, Union
from src.hypergraph import Node


class PersonalityNode(Node):
    """
    Representa um traço de personalidade do modelo FFM/HEXACO.
    """
    
    def __init__(self, node_id: Optional[str] = None, trait: str = "", value: float = 0.5):
        """
        Inicializa um nó de personalidade.
        
        Args:
            node_id: ID único do nó. Se não fornecido, um UUID será gerado.
            trait: Nome do traço de personalidade (ex: "HonestyHumility", "Extraversion").
            value: Valor do traço (entre 0 e 1).
        """
        super().__init__(node_id=node_id, node_type="Personality")
        self.trait = trait
        self.value = max(0.0, min(1.0, value))  # Garante que o valor esteja entre 0 e 1
        
    def to_dict(self) -> Dict[str, Any]:
        """
        Converte o nó para um dicionário.
        
        Returns:
            Um dicionário representando o nó.
        """
        data = super().to_dict()
        data.update({
            "trait": self.trait,
            "value": self.value
        })
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'PersonalityNode':
        """
        Cria um nó de personalidade a partir de um dicionário.
        
        Args:
            data: Dicionário contendo os dados do nó.
            
        Returns:
            Uma instância de PersonalityNode.
        """
        return cls(
            node_id=data.get("id"),
            trait=data.get("trait", ""),
            value=data.get("value", 0.5)
        )
    
    def __str__(self) -> str:
        return f"PersonalityNode(id={self.id}, trait={self.trait}, value={self.value:.2f})"


class ValueNode(Node):
    """
    Representa um valor do modelo de Schwartz/Scheler.
    """
    
    def __init__(self, node_id: Optional[str] = None, value_name: str = "", priority: float = 0.5):
        """
        Inicializa um nó de valor.
        
        Args:
            node_id: ID único do nó. Se não fornecido, um UUID será gerado.
            value_name: Nome do valor (ex: "Security", "Benevolence").
            priority: Prioridade do valor (entre 0 e 1).
        """
        super().__init__(node_id=node_id, node_type="Value")
        self.value_name = value_name
        self.priority = max(0.0, min(1.0, priority))  # Garante que a prioridade esteja entre 0 e 1
        
    def to_dict(self) -> Dict[str, Any]:
        """
        Converte o nó para um dicionário.
        
        Returns:
            Um dicionário representando o nó.
        """
        data = super().to_dict()
        data.update({
            "value_name": self.value_name,
            "priority": self.priority
        })
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ValueNode':
        """
        Cria um nó de valor a partir de um dicionário.
        
        Args:
            data: Dicionário contendo os dados do nó.
            
        Returns:
            Uma instância de ValueNode.
        """
        return cls(
            node_id=data.get("id"),
            value_name=data.get("value_name", ""),
            priority=data.get("priority", 0.5)
        )
    
    def __str__(self) -> str:
        return f"ValueNode(id={self.id}, value_name={self.value_name}, priority={self.priority:.2f})"


class NeedNode(Node):
    """
    Representa uma necessidade do modelo de Maslow/Bens Básicos.
    """
    
    def __init__(self, node_id: Optional[str] = None, need_name: str = "", satisfaction: float = 0.5):
        """
        Inicializa um nó de necessidade.
        
        Args:
            node_id: ID único do nó. Se não fornecido, um UUID será gerado.
            need_name: Nome da necessidade (ex: "Belonging", "Safety").
            satisfaction: Nível de satisfação da necessidade (entre 0 e 1).
        """
        super().__init__(node_id=node_id, node_type="Need")
        self.need_name = need_name
        self.satisfaction = max(0.0, min(1.0, satisfaction))  # Garante que a satisfação esteja entre 0 e 1
        
    def to_dict(self) -> Dict[str, Any]:
        """
        Converte o nó para um dicionário.
        
        Returns:
            Um dicionário representando o nó.
        """
        data = super().to_dict()
        data.update({
            "need_name": self.need_name,
            "satisfaction": self.satisfaction
        })
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'NeedNode':
        """
        Cria um nó de necessidade a partir de um dicionário.
        
        Args:
            data: Dicionário contendo os dados do nó.
            
        Returns:
            Uma instância de NeedNode.
        """
        return cls(
            node_id=data.get("id"),
            need_name=data.get("need_name", ""),
            satisfaction=data.get("satisfaction", 0.5)
        )
    
    def __str__(self) -> str:
        return f"NeedNode(id={self.id}, need_name={self.need_name}, satisfaction={self.satisfaction:.2f})"


class HabitNode(Node):
    """
    Representa uma virtude ou vício (hábito).
    """
    
    def __init__(self, node_id: Optional[str] = None, habit_name: str = "", strength: float = 0.5):
        """
        Inicializa um nó de hábito.
        
        Args:
            node_id: ID único do nó. Se não fornecido, um UUID será gerado.
            habit_name: Nome do hábito (ex: "Courage", "Patience").
            strength: Força do hábito (entre 0 e 1).
        """
        super().__init__(node_id=node_id, node_type="Habit")
        self.habit_name = habit_name
        self.strength = max(0.0, min(1.0, strength))  # Garante que a força esteja entre 0 e 1
        
    def to_dict(self) -> Dict[str, Any]:
        """
        Converte o nó para um dicionário.
        
        Returns:
            Um dicionário representando o nó.
        """
        data = super().to_dict()
        data.update({
            "habit_name": self.habit_name,
            "strength": self.strength
        })
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'HabitNode':
        """
        Cria um nó de hábito a partir de um dicionário.
        
        Args:
            data: Dicionário contendo os dados do nó.
            
        Returns:
            Uma instância de HabitNode.
        """
        return cls(
            node_id=data.get("id"),
            habit_name=data.get("habit_name", ""),
            strength=data.get("strength", 0.5)
        )
    
    def __str__(self) -> str:
        return f"HabitNode(id={self.id}, habit_name={self.habit_name}, strength={self.strength:.2f})"


class BeliefNode(Node):
    """
    Representa uma crença formada sobre o mundo ou sobre si mesmo.
    """
    
    def __init__(self, node_id: Optional[str] = None, content: str = "", confidence: float = 0.5):
        """
        Inicializa um nó de crença.
        
        Args:
            node_id: ID único do nó. Se não fornecido, um UUID será gerado.
            content: Conteúdo da crença (ex: "O mundo é perigoso").
            confidence: Nível de confiança na crença (entre 0 e 1).
        """
        super().__init__(node_id=node_id, node_type="Belief")
        self.content = content
        self.confidence = max(0.0, min(1.0, confidence))  # Garante que a confiança esteja entre 0 e 1
        
    def to_dict(self) -> Dict[str, Any]:
        """
        Converte o nó para um dicionário.
        
        Returns:
            Um dicionário representando o nó.
        """
        data = super().to_dict()
        data.update({
            "content": self.content,
            "confidence": self.confidence
        })
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'BeliefNode':
        """
        Cria um nó de crença a partir de um dicionário.
        
        Args:
            data: Dicionário contendo os dados do nó.
            
        Returns:
            Uma instância de BeliefNode.
        """
        return cls(
            node_id=data.get("id"),
            content=data.get("content", ""),
            confidence=data.get("confidence", 0.5)
        )
    
    def __str__(self) -> str:
        return f"BeliefNode(id={self.id}, content={self.content}, confidence={self.confidence:.2f})"

