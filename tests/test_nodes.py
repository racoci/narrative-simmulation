"""
Testes para os tipos específicos de nós do hiper-grafo.
"""

import sys
import os

# Adiciona o diretório pai ao path para importar os módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.nodes import PersonalityNode, ValueNode, NeedNode, HabitNode, BeliefNode

def test_personality_node():
    """Testa a criação e manipulação de nós de personalidade."""
    print("Testando PersonalityNode...")
    
    # Cria um nó de personalidade
    node = PersonalityNode(node_id="p1", trait="Extraversion", value=0.8)
    
    # Verifica os atributos
    assert node.id == "p1"
    assert node.type == "Personality"
    assert node.trait == "Extraversion"
    assert node.value == 0.8
    
    # Testa a conversão para dicionário
    node_dict = node.to_dict()
    assert node_dict["id"] == "p1"
    assert node_dict["type"] == "Personality"
    assert node_dict["trait"] == "Extraversion"
    assert node_dict["value"] == 0.8
    
    # Testa a criação a partir de um dicionário
    node2 = PersonalityNode.from_dict(node_dict)
    assert node2.id == "p1"
    assert node2.type == "Personality"
    assert node2.trait == "Extraversion"
    assert node2.value == 0.8
    
    print("Teste de PersonalityNode concluído com sucesso!")

def test_value_node():
    """Testa a criação e manipulação de nós de valor."""
    print("Testando ValueNode...")
    
    # Cria um nó de valor
    node = ValueNode(node_id="v1", value_name="Security", priority=0.9)
    
    # Verifica os atributos
    assert node.id == "v1"
    assert node.type == "Value"
    assert node.value_name == "Security"
    assert node.priority == 0.9
    
    # Testa a conversão para dicionário
    node_dict = node.to_dict()
    assert node_dict["id"] == "v1"
    assert node_dict["type"] == "Value"
    assert node_dict["value_name"] == "Security"
    assert node_dict["priority"] == 0.9
    
    # Testa a criação a partir de um dicionário
    node2 = ValueNode.from_dict(node_dict)
    assert node2.id == "v1"
    assert node2.type == "Value"
    assert node2.value_name == "Security"
    assert node2.priority == 0.9
    
    print("Teste de ValueNode concluído com sucesso!")

def test_need_node():
    """Testa a criação e manipulação de nós de necessidade."""
    print("Testando NeedNode...")
    
    # Cria um nó de necessidade
    node = NeedNode(node_id="n1", need_name="Belonging", satisfaction=0.7)
    
    # Verifica os atributos
    assert node.id == "n1"
    assert node.type == "Need"
    assert node.need_name == "Belonging"
    assert node.satisfaction == 0.7
    
    # Testa a conversão para dicionário
    node_dict = node.to_dict()
    assert node_dict["id"] == "n1"
    assert node_dict["type"] == "Need"
    assert node_dict["need_name"] == "Belonging"
    assert node_dict["satisfaction"] == 0.7
    
    # Testa a criação a partir de um dicionário
    node2 = NeedNode.from_dict(node_dict)
    assert node2.id == "n1"
    assert node2.type == "Need"
    assert node2.need_name == "Belonging"
    assert node2.satisfaction == 0.7
    
    print("Teste de NeedNode concluído com sucesso!")

def test_habit_node():
    """Testa a criação e manipulação de nós de hábito."""
    print("Testando HabitNode...")
    
    # Cria um nó de hábito
    node = HabitNode(node_id="h1", habit_name="Courage", strength=0.6)
    
    # Verifica os atributos
    assert node.id == "h1"
    assert node.type == "Habit"
    assert node.habit_name == "Courage"
    assert node.strength == 0.6
    
    # Testa a conversão para dicionário
    node_dict = node.to_dict()
    assert node_dict["id"] == "h1"
    assert node_dict["type"] == "Habit"
    assert node_dict["habit_name"] == "Courage"
    assert node_dict["strength"] == 0.6
    
    # Testa a criação a partir de um dicionário
    node2 = HabitNode.from_dict(node_dict)
    assert node2.id == "h1"
    assert node2.type == "Habit"
    assert node2.habit_name == "Courage"
    assert node2.strength == 0.6
    
    print("Teste de HabitNode concluído com sucesso!")

def test_belief_node():
    """Testa a criação e manipulação de nós de crença."""
    print("Testando BeliefNode...")
    
    # Cria um nó de crença
    node = BeliefNode(node_id="b1", content="O mundo é perigoso", confidence=0.85)
    
    # Verifica os atributos
    assert node.id == "b1"
    assert node.type == "Belief"
    assert node.content == "O mundo é perigoso"
    assert node.confidence == 0.85
    
    # Testa a conversão para dicionário
    node_dict = node.to_dict()
    assert node_dict["id"] == "b1"
    assert node_dict["type"] == "Belief"
    assert node_dict["content"] == "O mundo é perigoso"
    assert node_dict["confidence"] == 0.85
    
    # Testa a criação a partir de um dicionário
    node2 = BeliefNode.from_dict(node_dict)
    assert node2.id == "b1"
    assert node2.type == "Belief"
    assert node2.content == "O mundo é perigoso"
    assert node2.confidence == 0.85
    
    print("Teste de BeliefNode concluído com sucesso!")

def run_tests():
    """Executa todos os testes."""
    test_personality_node()
    test_value_node()
    test_need_node()
    test_habit_node()
    test_belief_node()
    print("Todos os testes concluídos com sucesso!")

if __name__ == "__main__":
    run_tests()

