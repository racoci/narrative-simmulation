"""
Testes para o módulo de mundo.
"""

import sys
import os

# Adiciona o diretório pai ao path para importar os módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.world import Entity, Location, WorldModule

def test_entity():
    """Testa a criação e manipulação de entidades."""
    print("Testando Entity...")
    
    # Cria uma entidade
    entity = Entity(
        entity_id="e1",
        entity_type="TestEntity",
        name="Test Entity",
        position={"x": 10.0, "y": 20.0, "z": 30.0},
        properties={"color": "red", "size": "large"}
    )
    
    # Verifica os atributos
    assert entity.id == "e1"
    assert entity.type == "TestEntity"
    assert entity.name == "Test Entity"
    assert entity.position == {"x": 10.0, "y": 20.0, "z": 30.0}
    assert entity.properties == {"color": "red", "size": "large"}
    
    # Testa a conversão para dicionário
    entity_dict = entity.to_dict()
    assert entity_dict["id"] == "e1"
    assert entity_dict["type"] == "TestEntity"
    assert entity_dict["name"] == "Test Entity"
    assert entity_dict["position"] == {"x": 10.0, "y": 20.0, "z": 30.0}
    assert entity_dict["properties"] == {"color": "red", "size": "large"}
    
    # Testa a criação a partir de um dicionário
    entity2 = Entity.from_dict(entity_dict)
    assert entity2.id == "e1"
    assert entity2.type == "TestEntity"
    assert entity2.name == "Test Entity"
    assert entity2.position == {"x": 10.0, "y": 20.0, "z": 30.0}
    assert entity2.properties == {"color": "red", "size": "large"}
    
    print("Teste de Entity concluído com sucesso!")

def test_location():
    """Testa a criação e manipulação de locais."""
    print("Testando Location...")
    
    # Cria um local
    location = Location(
        entity_id="l1",
        name="Test Location",
        position={"x": 0.0, "y": 0.0, "z": 0.0},
        properties={"type": "room", "access": "public"},
        area={"width": 20.0, "height": 10.0, "depth": 5.0}
    )
    
    # Verifica os atributos
    assert location.id == "l1"
    assert location.type == "Location"
    assert location.name == "Test Location"
    assert location.position == {"x": 0.0, "y": 0.0, "z": 0.0}
    assert location.properties == {"type": "room", "access": "public"}
    assert location.area == {"width": 20.0, "height": 10.0, "depth": 5.0}
    
    # Testa o método contains
    # Ponto dentro do local
    assert location.contains({"x": 5.0, "y": 2.0, "z": 1.0}) == True
    
    # Pontos fora do local
    assert location.contains({"x": 15.0, "y": 6.0, "z": 3.0}) == False  # Fora nos três eixos
    assert location.contains({"x": 0.0, "y": 0.0, "z": 10.0}) == False  # Fora no eixo z
    
    # Testa a conversão para dicionário
    location_dict = location.to_dict()
    assert location_dict["id"] == "l1"
    assert location_dict["type"] == "Location"
    assert location_dict["name"] == "Test Location"
    assert location_dict["position"] == {"x": 0.0, "y": 0.0, "z": 0.0}
    assert location_dict["properties"] == {"type": "room", "access": "public"}
    assert location_dict["area"] == {"width": 20.0, "height": 10.0, "depth": 5.0}
    
    # Testa a criação a partir de um dicionário
    location2 = Location.from_dict(location_dict)
    assert location2.id == "l1"
    assert location2.type == "Location"
    assert location2.name == "Test Location"
    assert location2.position == {"x": 0.0, "y": 0.0, "z": 0.0}
    assert location2.properties == {"type": "room", "access": "public"}
    assert location2.area == {"width": 20.0, "height": 10.0, "depth": 5.0}
    
    print("Teste de Location concluído com sucesso!")

def test_world_module():
    """Testa a criação e manipulação do módulo de mundo."""
    print("Testando WorldModule...")
    
    # Cria um módulo de mundo
    world = WorldModule()
    
    # Verifica os atributos iniciais
    assert len(world.entities) == 0
    assert len(world.locations) == 0
    assert world.current_time == 0
    
    # Cria e adiciona locais primeiro
    location1 = Location(
        entity_id="l1",
        name="Location 1",
        position={"x": 0.0, "y": 0.0, "z": 0.0},
        area={"width": 10.0, "height": 10.0, "depth": 10.0}
    )
    
    location2 = Location(
        entity_id="l2",
        name="Location 2",
        position={"x": 20.0, "y": 0.0, "z": 0.0},
        area={"width": 10.0, "height": 10.0, "depth": 10.0}
    )
    
    world.add_entity(location1)
    world.add_entity(location2)
    
    # Verifica se os locais foram adicionados
    assert len(world.entities) == 2
    assert len(world.locations) == 2
    assert world.get_entity("l1") == location1
    assert world.get_entity("l2") == location2
    assert world.locations["l1"] == location1
    assert world.locations["l2"] == location2
    
    # Cria e adiciona entidades
    entity1 = Entity(entity_id="e1", name="Entity 1", position={"x": 0.0, "y": 0.0, "z": 0.0})
    entity2 = Entity(entity_id="e2", name="Entity 2", position={"x": 20.0, "y": 0.0, "z": 0.0})
    
    world.add_entity(entity1)
    world.add_entity(entity2)
    
    # Verifica se as entidades foram adicionadas
    assert len(world.entities) == 4
    assert world.get_entity("e1") == entity1
    assert world.get_entity("e2") == entity2
    
    # Testa a obtenção do local de uma entidade
    location_of_e1 = world.get_location_of_entity("e1")
    assert location_of_e1 == location1  # entity1 está em location1
    
    location_of_e2 = world.get_location_of_entity("e2")
    assert location_of_e2 == location2  # entity2 está em location2
    
    # Testa a obtenção de entidades em um local
    entities_in_l1 = world.get_entities_at_location("l1")
    assert len(entities_in_l1) == 1
    assert entities_in_l1[0].id == "e1"
    
    # Testa a percepção do mundo
    perception = world.perceive("e1")
    assert perception["position"] == entity1.position
    assert perception["location"] == location1.to_dict()
    
    # Testa a execução de ações
    # Ação de movimento
    action_result = world.act("e1", {
        "type": "move",
        "position": {"x": 20.0, "y": 0.0, "z": 0.0}
    })
    
    assert action_result["success"] == True
    assert action_result["new_position"] == {"x": 20.0, "y": 0.0, "z": 0.0}
    assert action_result["location"] == location2  # entity1 agora está em location2
    
    # Verifica se a posição da entidade foi atualizada
    assert world.get_entity("e1").position == {"x": 20.0, "y": 0.0, "z": 0.0}
    assert world.get_location_of_entity("e1") == location2
    
    # Testa a atualização do mundo
    world.update(100)
    assert world.current_time == 100
    
    # Testa a remoção de uma entidade
    world.remove_entity("e2")
    assert len(world.entities) == 3
    assert world.get_entity("e2") is None
    
    # Testa a remoção de um local
    world.remove_entity("l2")
    assert len(world.entities) == 2
    assert len(world.locations) == 1
    assert world.get_entity("l2") is None
    assert "l2" not in world.locations
    
    # Testa a conversão para dicionário
    world_dict = world.to_dict()
    assert world_dict["time"] == 100
    assert len(world_dict["entities"]) == 2
    assert len(world_dict["locations"]) == 1
    
    print("Teste de WorldModule concluído com sucesso!")

def run_tests():
    """Executa todos os testes."""
    test_entity()
    test_location()
    test_world_module()
    print("Todos os testes concluídos com sucesso!")

if __name__ == "__main__":
    run_tests()

