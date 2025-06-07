"""
Testes para os tipos específicos de hiper-arestas do hiper-grafo.
"""

import sys
import os

# Adiciona o diretório pai ao path para importar os módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.edges import MemoryEdge, EmotionEdge, RuleEdge

def test_memory_edge():
    """Testa a criação e manipulação de hiper-arestas de memória."""
    print("Testando MemoryEdge...")
    
    # Cria uma hiper-aresta de memória
    edge = MemoryEdge(
        edge_id="m1",
        nodes=["n1", "n2", "n3"],
        emotion_tag="Fear",
        intensity=0.9,
        salience=0.8,
        is_cornerstone=True,
        timestamp=1000,
        description="Um evento traumático"
    )
    
    # Verifica os atributos
    assert edge.id == "m1"
    assert edge.type == "Memory"
    assert edge.nodes == ["n1", "n2", "n3"]
    assert edge.emotion_tag == "Fear"
    assert edge.intensity == 0.9
    assert edge.salience == 0.8
    assert edge.is_cornerstone == True
    assert edge.timestamp == 1000
    assert edge.description == "Um evento traumático"
    
    # Testa a conversão para dicionário
    edge_dict = edge.to_dict()
    assert edge_dict["id"] == "m1"
    assert edge_dict["type"] == "Memory"
    assert edge_dict["nodes"] == ["n1", "n2", "n3"]
    assert edge_dict["emotion_tag"] == "Fear"
    assert edge_dict["intensity"] == 0.9
    assert edge_dict["salience"] == 0.8
    assert edge_dict["is_cornerstone"] == True
    assert edge_dict["timestamp"] == 1000
    assert edge_dict["description"] == "Um evento traumático"
    
    # Testa a criação a partir de um dicionário
    edge2 = MemoryEdge.from_dict(edge_dict)
    assert edge2.id == "m1"
    assert edge2.type == "Memory"
    assert edge2.nodes == ["n1", "n2", "n3"]
    assert edge2.emotion_tag == "Fear"
    assert edge2.intensity == 0.9
    assert edge2.salience == 0.8
    assert edge2.is_cornerstone == True
    assert edge2.timestamp == 1000
    assert edge2.description == "Um evento traumático"
    
    print("Teste de MemoryEdge concluído com sucesso!")

def test_emotion_edge():
    """Testa a criação e manipulação de hiper-arestas de emoção."""
    print("Testando EmotionEdge...")
    
    # Cria uma hiper-aresta de emoção
    edge = EmotionEdge(
        edge_id="e1",
        nodes=["n1", "n2"],
        emotion="Anger",
        target="n3",
        decay_rate=0.2,
        intensity=0.7,
        timestamp=1000
    )
    
    # Verifica os atributos
    assert edge.id == "e1"
    assert edge.type == "Emotion"
    assert edge.nodes == ["n1", "n2"]
    assert edge.emotion == "Anger"
    assert edge.target == "n3"
    assert edge.decay_rate == 0.2
    assert edge.intensity == 0.7
    assert edge.timestamp == 1000
    
    # Testa a atualização da intensidade
    edge.update_intensity(1005)  # 5 unidades de tempo depois
    assert edge.intensity < 0.7  # A intensidade deve ter diminuído
    assert edge.timestamp == 1005  # O timestamp deve ter sido atualizado
    
    # Testa a conversão para dicionário
    edge_dict = edge.to_dict()
    assert edge_dict["id"] == "e1"
    assert edge_dict["type"] == "Emotion"
    assert edge_dict["nodes"] == ["n1", "n2"]
    assert edge_dict["emotion"] == "Anger"
    assert edge_dict["target"] == "n3"
    assert edge_dict["decay_rate"] == 0.2
    assert edge_dict["intensity"] < 0.7  # A intensidade foi atualizada
    assert edge_dict["timestamp"] == 1005
    
    # Testa a criação a partir de um dicionário
    edge2 = EmotionEdge.from_dict(edge_dict)
    assert edge2.id == "e1"
    assert edge2.type == "Emotion"
    assert edge2.nodes == ["n1", "n2"]
    assert edge2.emotion == "Anger"
    assert edge2.target == "n3"
    assert edge2.decay_rate == 0.2
    assert abs(edge2.intensity - edge_dict["intensity"]) < 1e-10  # Comparação de ponto flutuante
    assert edge2.timestamp == 1005
    
    print("Teste de EmotionEdge concluído com sucesso!")

def test_rule_edge():
    """Testa a criação e manipulação de hiper-arestas de regra."""
    print("Testando RuleEdge...")
    
    # Cria uma hiper-aresta de regra
    edge = RuleEdge(
        edge_id="r1",
        nodes=["n1", "n2"],
        trigger="MemoryEdge(type=Betrayal)",
        action="decrease_priority(ValueNode:Benevolence, 0.2)",
        confidence=0.75
    )
    
    # Verifica os atributos
    assert edge.id == "r1"
    assert edge.type == "Rule"
    assert edge.nodes == ["n1", "n2"]
    assert edge.trigger == "MemoryEdge(type=Betrayal)"
    assert edge.action == "decrease_priority(ValueNode:Benevolence, 0.2)"
    assert edge.confidence == 0.75
    
    # Testa a conversão para dicionário
    edge_dict = edge.to_dict()
    assert edge_dict["id"] == "r1"
    assert edge_dict["type"] == "Rule"
    assert edge_dict["nodes"] == ["n1", "n2"]
    assert edge_dict["trigger"] == "MemoryEdge(type=Betrayal)"
    assert edge_dict["action"] == "decrease_priority(ValueNode:Benevolence, 0.2)"
    assert edge_dict["confidence"] == 0.75
    
    # Testa a criação a partir de um dicionário
    edge2 = RuleEdge.from_dict(edge_dict)
    assert edge2.id == "r1"
    assert edge2.type == "Rule"
    assert edge2.nodes == ["n1", "n2"]
    assert edge2.trigger == "MemoryEdge(type=Betrayal)"
    assert edge2.action == "decrease_priority(ValueNode:Benevolence, 0.2)"
    assert edge2.confidence == 0.75
    
    print("Teste de RuleEdge concluído com sucesso!")

def run_tests():
    """Executa todos os testes."""
    test_memory_edge()
    test_emotion_edge()
    test_rule_edge()
    print("Todos os testes concluídos com sucesso!")

if __name__ == "__main__":
    run_tests()

