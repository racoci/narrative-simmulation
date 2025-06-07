"""
Módulo que implementa o mundo da simulação.
"""

from typing import Dict, List, Any, Optional, Set, Union
import uuid


class Entity:
    """
    Classe base para todas as entidades no mundo.
    """
    
    def __init__(self, entity_id: Optional[str] = None, entity_type: str = "Entity", 
                 name: str = "", position: Optional[Dict[str, float]] = None,
                 properties: Optional[Dict[str, Any]] = None):
        """
        Inicializa uma entidade.
        
        Args:
            entity_id: ID único da entidade. Se não fornecido, um UUID será gerado.
            entity_type: Tipo da entidade.
            name: Nome da entidade.
            position: Posição da entidade no mundo (dicionário com coordenadas).
            properties: Propriedades adicionais da entidade.
        """
        self.id = entity_id if entity_id else str(uuid.uuid4())
        self.type = entity_type
        self.name = name
        self.position = position if position else {"x": 0.0, "y": 0.0, "z": 0.0}
        self.properties = properties if properties else {}
        
    def to_dict(self) -> Dict[str, Any]:
        """
        Converte a entidade para um dicionário.
        
        Returns:
            Um dicionário representando a entidade.
        """
        return {
            "id": self.id,
            "type": self.type,
            "name": self.name,
            "position": self.position,
            "properties": self.properties
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Entity':
        """
        Cria uma entidade a partir de um dicionário.
        
        Args:
            data: Dicionário contendo os dados da entidade.
            
        Returns:
            Uma instância de Entity.
        """
        return cls(
            entity_id=data.get("id"),
            entity_type=data.get("type", "Entity"),
            name=data.get("name", ""),
            position=data.get("position", {"x": 0.0, "y": 0.0, "z": 0.0}),
            properties=data.get("properties", {})
        )
    
    def __str__(self) -> str:
        return f"{self.type}(id={self.id}, name={self.name})"


class Location(Entity):
    """
    Representa um local no mundo.
    """
    
    def __init__(self, entity_id: Optional[str] = None, name: str = "", 
                 position: Optional[Dict[str, float]] = None,
                 properties: Optional[Dict[str, Any]] = None,
                 area: Optional[Dict[str, float]] = None):
        """
        Inicializa um local.
        
        Args:
            entity_id: ID único do local. Se não fornecido, um UUID será gerado.
            name: Nome do local.
            position: Posição do local no mundo (dicionário com coordenadas).
            properties: Propriedades adicionais do local.
            area: Área do local (dicionário com dimensões).
        """
        super().__init__(entity_id=entity_id, entity_type="Location", name=name, 
                         position=position, properties=properties)
        self.area = area if area else {"width": 10.0, "height": 10.0, "depth": 10.0}
        
    def contains(self, position: Dict[str, float]) -> bool:
        """
        Verifica se uma posição está dentro deste local.
        
        Args:
            position: Posição a ser verificada.
            
        Returns:
            True se a posição estiver dentro do local, False caso contrário.
        """
        # Calcula os limites do local
        min_x = self.position["x"] - self.area["width"] / 2
        max_x = self.position["x"] + self.area["width"] / 2
        min_y = self.position["y"] - self.area["height"] / 2
        max_y = self.position["y"] + self.area["height"] / 2
        min_z = self.position["z"] - self.area["depth"] / 2
        max_z = self.position["z"] + self.area["depth"] / 2
        
        # Verifica se a posição está dentro dos limites
        return (min_x <= position["x"] <= max_x and
                min_y <= position["y"] <= max_y and
                min_z <= position["z"] <= max_z)
        
    def to_dict(self) -> Dict[str, Any]:
        """
        Converte o local para um dicionário.
        
        Returns:
            Um dicionário representando o local.
        """
        data = super().to_dict()
        data.update({
            "area": self.area
        })
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Location':
        """
        Cria um local a partir de um dicionário.
        
        Args:
            data: Dicionário contendo os dados do local.
            
        Returns:
            Uma instância de Location.
        """
        return cls(
            entity_id=data.get("id"),
            name=data.get("name", ""),
            position=data.get("position", {"x": 0.0, "y": 0.0, "z": 0.0}),
            properties=data.get("properties", {}),
            area=data.get("area", {"width": 10.0, "height": 10.0, "depth": 10.0})
        )


class WorldModule:
    """
    Classe que implementa o módulo de mundo.
    Gerencia o estado do ambiente de simulação.
    """
    
    def __init__(self):
        """
        Inicializa o módulo de mundo.
        """
        self.entities: Dict[str, Entity] = {}
        self.locations: Dict[str, Location] = {}
        self.current_time = 0
        
    def add_entity(self, entity: Entity) -> None:
        """
        Adiciona uma entidade ao mundo.
        
        Args:
            entity: Entidade a ser adicionada.
        """
        self.entities[entity.id] = entity
        
        # Se for um local, adiciona também à lista de locais
        if isinstance(entity, Location):
            self.locations[entity.id] = entity
            
    def remove_entity(self, entity_id: str) -> None:
        """
        Remove uma entidade do mundo.
        
        Args:
            entity_id: ID da entidade a ser removida.
        """
        if entity_id in self.entities:
            entity = self.entities[entity_id]
            del self.entities[entity_id]
            
            # Se for um local, remove também da lista de locais
            if isinstance(entity, Location) and entity_id in self.locations:
                del self.locations[entity_id]
                
    def get_entity(self, entity_id: str) -> Optional[Entity]:
        """
        Obtém uma entidade pelo seu ID.
        
        Args:
            entity_id: ID da entidade a ser obtida.
            
        Returns:
            A entidade correspondente ao ID, ou None se não existir.
        """
        return self.entities.get(entity_id)
    
    def get_entities_at_location(self, location_id: str) -> List[Entity]:
        """
        Obtém todas as entidades em um determinado local.
        
        Args:
            location_id: ID do local.
            
        Returns:
            Lista de entidades no local.
        """
        location = self.locations.get(location_id)
        if not location:
            return []
            
        return [entity for entity in self.entities.values() 
                if location.contains(entity.position)]
    
    def get_location_of_entity(self, entity_id: str) -> Optional[Location]:
        """
        Obtém o local onde uma entidade está.
        
        Args:
            entity_id: ID da entidade.
            
        Returns:
            O local onde a entidade está, ou None se não estiver em nenhum local.
        """
        entity = self.get_entity(entity_id)
        if not entity:
            return None
            
        for location in self.locations.values():
            if location.contains(entity.position):
                return location
                
        return None
    
    def perceive(self, agent_id: str, area: Optional[Dict[str, float]] = None) -> Dict[str, Any]:
        """
        Retorna a percepção do mundo para um agente.
        
        Args:
            agent_id: ID do agente.
            area: Área de percepção (opcional). Se não fornecida, usa a posição do agente.
            
        Returns:
            Um dicionário contendo a percepção do mundo.
        """
        agent = self.get_entity(agent_id)
        if not agent:
            return {"error": "Agent not found"}
            
        # Se não foi fornecida uma área, usa a posição do agente
        if not area:
            # Área padrão ao redor do agente
            area = {
                "center": agent.position,
                "radius": 10.0
            }
            
        # Calcula a distância entre dois pontos
        def distance(pos1, pos2):
            return ((pos1["x"] - pos2["x"]) ** 2 + 
                    (pos1["y"] - pos2["y"]) ** 2 + 
                    (pos1["z"] - pos2["z"]) ** 2) ** 0.5
            
        # Filtra as entidades que estão dentro da área de percepção
        perceived_entities = []
        for entity in self.entities.values():
            if entity.id != agent_id:  # Não inclui o próprio agente
                if distance(entity.position, area["center"]) <= area["radius"]:
                    perceived_entities.append(entity.to_dict())
                    
        # Obtém o local atual do agente
        current_location = self.get_location_of_entity(agent_id)
        
        return {
            "time": self.current_time,
            "position": agent.position,
            "location": current_location.to_dict() if current_location else None,
            "entities": perceived_entities
        }
    
    def act(self, agent_id: str, action: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executa uma ação de um agente no mundo.
        
        Args:
            agent_id: ID do agente.
            action: Dicionário descrevendo a ação.
            
        Returns:
            Um dicionário contendo o resultado da ação.
        """
        agent = self.get_entity(agent_id)
        if not agent:
            return {"success": False, "error": "Agent not found"}
            
        action_type = action.get("type")
        
        if action_type == "move":
            # Ação de movimento
            new_position = action.get("position")
            if not new_position:
                return {"success": False, "error": "No position specified"}
                
            # Atualiza a posição do agente
            agent.position = new_position
            
            return {
                "success": True,
                "new_position": new_position,
                "location": self.get_location_of_entity(agent_id)
            }
            
        elif action_type == "interact":
            # Ação de interação com outra entidade
            target_id = action.get("target")
            if not target_id:
                return {"success": False, "error": "No target specified"}
                
            target = self.get_entity(target_id)
            if not target:
                return {"success": False, "error": "Target not found"}
                
            # Verifica se o alvo está próximo o suficiente
            distance = ((agent.position["x"] - target.position["x"]) ** 2 + 
                        (agent.position["y"] - target.position["y"]) ** 2 + 
                        (agent.position["z"] - target.position["z"]) ** 2) ** 0.5
                
            if distance > action.get("max_distance", 2.0):
                return {"success": False, "error": "Target too far away"}
                
            # Executa a interação (aqui seria implementada a lógica específica)
            interaction = action.get("interaction", {})
            
            return {
                "success": True,
                "target": target.to_dict(),
                "interaction": interaction
            }
            
        else:
            return {"success": False, "error": f"Unknown action type: {action_type}"}
    
    def update(self, current_time: int) -> None:
        """
        Atualiza o estado do mundo.
        
        Args:
            current_time: Tempo atual da simulação.
        """
        self.current_time = current_time
        
        # Aqui seriam implementadas atualizações específicas do mundo,
        # como eventos ambientais, mudanças de estado, etc.
        
    def to_dict(self) -> Dict[str, Any]:
        """
        Converte o mundo para um dicionário.
        
        Returns:
            Um dicionário representando o mundo.
        """
        return {
            "time": self.current_time,
            "entities": [entity.to_dict() for entity in self.entities.values()],
            "locations": [location.to_dict() for location in self.locations.values()]
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'WorldModule':
        """
        Cria um mundo a partir de um dicionário.
        
        Args:
            data: Dicionário contendo os dados do mundo.
            
        Returns:
            Uma instância de WorldModule.
        """
        world = cls()
        world.current_time = data.get("time", 0)
        
        # Adiciona as entidades
        for entity_data in data.get("entities", []):
            entity_type = entity_data.get("type")
            
            if entity_type == "Location":
                entity = Location.from_dict(entity_data)
            else:
                entity = Entity.from_dict(entity_data)
                
            world.add_entity(entity)
            
        return world

