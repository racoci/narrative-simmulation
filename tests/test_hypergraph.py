"""
Testes básicos para as estruturas de dados do hiper-grafo.
"""

import sys
import os

# Adiciona o diretório pai ao path para importar os módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.hypergraph import Node, Hyperedge, Hypergraph

def test_node():
    """Testa a criação e manipulação de nós."""
    print("Testando Node...")
    
    # Cria um nó
    node = Node(node_id="n1", node_type="TestNode")
    
    # Verifica os atributos
    assert node.id == "n1"
    assert node.type == "TestNode"
    
    # Testa a conversão para dicionário
    node_dict = node.to_dict()
    assert node_dict["id"] == "n1"
    assert node_dict["type"] == "TestNode"
    
    # Testa a criação a partir de um dicionário
    node2 = Node.from_dict(node_dict)
    assert node2.id == "n1"
    assert node2.type == "TestNode"
    
    print("Teste de Node concluído com sucesso!")

def test_hyperedge():
    """Testa a criação e manipulação de hiper-arestas."""
    print("Testando Hyperedge...")
    
    # Cria uma hiper-aresta
    edge = Hyperedge(edge_id="e1", edge_type="TestEdge", nodes=["n1", "n2", "n3"])
    
    # Verifica os atributos
    assert edge.id == "e1"
    assert edge.type == "TestEdge"
    assert edge.nodes == ["n1", "n2", "n3"]
    
    # Testa a adição de nós
    edge.add_node("n4")
    assert "n4" in edge.nodes
    
    # Testa a remoção de nós
    edge.remove_node("n2")
    assert "n2" not in edge.nodes
    
    # Testa a conversão para dicionário
    edge_dict = edge.to_dict()
    assert edge_dict["id"] == "e1"
    assert edge_dict["type"] == "TestEdge"
    assert edge_dict["nodes"] == ["n1", "n3", "n4"]
    
    # Testa a criação a partir de um dicionário
    edge2 = Hyperedge.from_dict(edge_dict)
    assert edge2.id == "e1"
    assert edge2.type == "TestEdge"
    assert edge2.nodes == ["n1", "n3", "n4"]
    
    print("Teste de Hyperedge concluído com sucesso!")

def test_hypergraph():
    """Testa a criação e manipulação de hiper-grafos."""
    print("Testando Hypergraph...")
    
    # Cria um hiper-grafo
    graph = Hypergraph(graph_id="g1", name="TestGraph")
    
    # Verifica os atributos
    assert graph.id == "g1"
    assert graph.name == "TestGraph"
    
    # Cria alguns nós
    node1 = Node(node_id="n1", node_type="TestNode1")
    node2 = Node(node_id="n2", node_type="TestNode2")
    node3 = Node(node_id="n3", node_type="TestNode3")
    
    # Adiciona os nós ao grafo
    graph.add_node(node1)
    graph.add_node(node2)
    graph.add_node(node3)
    
    # Verifica se os nós foram adicionados
    assert len(graph.nodes) == 3
    assert graph.get_node("n1") == node1
    assert graph.get_node("n2") == node2
    assert graph.get_node("n3") == node3
    
    # Cria uma hiper-aresta
    edge = Hyperedge(edge_id="e1", edge_type="TestEdge", nodes=["n1", "n2"])
    
    # Adiciona a hiper-aresta ao grafo
    graph.add_edge(edge)
    
    # Verifica se a hiper-aresta foi adicionada
    assert len(graph.edges) == 1
    assert graph.get_edge("e1") == edge
    
    # Testa a obtenção de hiper-arestas para um nó
    edges_for_n1 = graph.get_edges_for_node("n1")
    assert len(edges_for_n1) == 1
    assert edges_for_n1[0] == edge
    
    # Testa a obtenção de nós conectados
    connected_to_n1 = graph.get_connected_nodes("n1")
    assert len(connected_to_n1) == 1
    assert "n2" in connected_to_n1
    
    # Testa a remoção de um nó
    graph.remove_node("n3")
    assert len(graph.nodes) == 2
    assert graph.get_node("n3") is None
    
    # Testa a remoção de uma hiper-aresta
    graph.remove_edge("e1")
    assert len(graph.edges) == 0
    assert graph.get_edge("e1") is None
    
    # Testa a conversão para dicionário
    graph_dict = graph.to_dict()
    assert graph_dict["id"] == "g1"
    assert graph_dict["name"] == "TestGraph"
    assert len(graph_dict["nodes"]) == 2
    assert len(graph_dict["edges"]) == 0
    
    # Testa a criação a partir de um dicionário
    graph2 = Hypergraph.from_dict(graph_dict)
    assert graph2.id == "g1"
    assert graph2.name == "TestGraph"
    assert len(graph2.nodes) == 2
    assert len(graph2.edges) == 0
    
    print("Teste de Hypergraph concluído com sucesso!")

def run_tests():
    """Executa todos os testes."""
    test_node()
    test_hyperedge()
    test_hypergraph()
    print("Todos os testes concluídos com sucesso!")

if __name__ == "__main__":
    run_tests()

