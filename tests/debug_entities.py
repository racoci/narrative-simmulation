"""
Teste de depuração para o método get_entities_at_location.
"""

import sys
import os

# Adiciona o diretório pai ao path para importar os módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.world import Entity, Location, WorldModule

def test_get_entities_at_location():
    """Testa o método get_entities_at_location."""
    
    # Cria um módulo de mundo
    world = WorldModule()
    
    # Cria e adiciona locais
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
    
    print(f"Locais adicionados: {len(world.locations)}")
    print(f"Location 1 limites: x=[{location1.position['x'] - location1.area['width']/2}, {location1.position['x'] + location1.area['width']/2}]")
    print(f"Location 2 limites: x=[{location2.position['x'] - location2.area['width']/2}, {location2.position['x'] + location2.area['width']/2}]")
    
    # Cria e adiciona entidades
    entity1 = Entity(entity_id="e1", name="Entity 1", position={"x": 0.0, "y": 0.0, "z": 0.0})
    entity2 = Entity(entity_id="e2", name="Entity 2", position={"x": 20.0, "y": 0.0, "z": 0.0})
    
    world.add_entity(entity1)
    world.add_entity(entity2)
    
    print(f"Entidades adicionadas: {len(world.entities)}")
    print(f"Entity 1 posição: {entity1.position}")
    print(f"Entity 2 posição: {entity2.position}")
    
    # Testa se as entidades estão nos locais corretos
    print(f"Entity 1 está em location 1: {location1.contains(entity1.position)}")
    print(f"Entity 1 está em location 2: {location2.contains(entity1.position)}")
    print(f"Entity 2 está em location 1: {location1.contains(entity2.position)}")
    print(f"Entity 2 está em location 2: {location2.contains(entity2.position)}")
    
    # Testa a obtenção de entidades em um local
    entities_in_l1 = world.get_entities_at_location("l1")
    entities_in_l2 = world.get_entities_at_location("l2")
    
    print(f"Entidades em location 1: {len(entities_in_l1)}")
    for entity in entities_in_l1:
        print(f"  - {entity.id}: {entity.name} at {entity.position}")
    
    print(f"Entidades em location 2: {len(entities_in_l2)}")
    for entity in entities_in_l2:
        print(f"  - {entity.id}: {entity.name} at {entity.position}")

if __name__ == "__main__":
    test_get_entities_at_location()

