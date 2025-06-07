"""
Módulo base para as estruturas de dados do hiper-grafo.
Contém as classes Node, Hyperedge e Hypergraph.
"""

from typing import Dict, List, Any, Optional, Set, Union
import uuid
import json


class Node:
    """
    Classe base para todos os nós do hiper-grafo.
    Um nó representa um conceito ou entidade na psique do personagem.
    """
    
    def __init__(self, node_id: Optional[str] = None, node_type: str = "Node"):
        """
        Inicializa um nó com um ID único e um tipo.
        
        Args:
            node_id: ID único do nó. Se não fornecido, um UUID será gerado.
            node_type: Tipo do nó (ex: "Personality", "Value", "Need", etc.)
        """
        self.id = node_id if node_id else str(uuid.uuid4())
        self.type = node_type
        
    def to_dict(self) -> Dict[str, Any]:
        """
        Converte o nó para um dicionário.
        
        Returns:
            Um dicionário representando o nó.
        """
        return {
            "id": self.id,
            "type": self.type
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Node':
        """
        Cria um nó a partir de um dicionário.
        
        Args:
            data: Dicionário contendo os dados do nó.
            
        Returns:
            Uma instância de Node.
        """
        return cls(node_id=data.get("id"), node_type=data.get("type", "Node"))
    
    def __str__(self) -> str:
        return f"{self.type}(id={self.id})"
    
    def __repr__(self) -> str:
        return self.__str__()


class Hyperedge:
    """
    Classe base para todas as hiper-arestas do hiper-grafo.
    Uma hiper-aresta representa uma relação complexa entre múltiplos nós.
    """
    
    def __init__(self, edge_id: Optional[str] = None, edge_type: str = "Hyperedge", 
                 nodes: Optional[List[str]] = None):
        """
        Inicializa uma hiper-aresta com um ID único, um tipo e uma lista de nós.
        
        Args:
            edge_id: ID único da hiper-aresta. Se não fornecido, um UUID será gerado.
            edge_type: Tipo da hiper-aresta (ex: "Memory", "Emotion", "Rule", etc.)
            nodes: Lista de IDs dos nós conectados por esta hiper-aresta.
        """
        self.id = edge_id if edge_id else str(uuid.uuid4())
        self.type = edge_type
        self.nodes = nodes if nodes else []
        
    def add_node(self, node_id: str) -> None:
        """
        Adiciona um nó à hiper-aresta.
        
        Args:
            node_id: ID do nó a ser adicionado.
        """
        if node_id not in self.nodes:
            self.nodes.append(node_id)
            
    def remove_node(self, node_id: str) -> None:
        """
        Remove um nó da hiper-aresta.
        
        Args:
            node_id: ID do nó a ser removido.
        """
        if node_id in self.nodes:
            self.nodes.remove(node_id)
            
    def to_dict(self) -> Dict[str, Any]:
        """
        Converte a hiper-aresta para um dicionário.
        
        Returns:
            Um dicionário representando a hiper-aresta.
        """
        return {
            "id": self.id,
            "type": self.type,
            "nodes": self.nodes
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Hyperedge':
        """
        Cria uma hiper-aresta a partir de um dicionário.
        
        Args:
            data: Dicionário contendo os dados da hiper-aresta.
            
        Returns:
            Uma instância de Hyperedge.
        """
        return cls(
            edge_id=data.get("id"),
            edge_type=data.get("type", "Hyperedge"),
            nodes=data.get("nodes", [])
        )
    
    def __str__(self) -> str:
        return f"{self.type}(id={self.id}, nodes={len(self.nodes)})"
    
    def __repr__(self) -> str:
        return self.__str__()


class Hypergraph:
    """
    Classe que representa um hiper-grafo completo.
    Um hiper-grafo é uma coleção de nós e hiper-arestas.
    """
    
    def __init__(self, graph_id: Optional[str] = None, name: str = "Hypergraph"):
        """
        Inicializa um hiper-grafo com um ID único e um nome.
        
        Args:
            graph_id: ID único do hiper-grafo. Se não fornecido, um UUID será gerado.
            name: Nome do hiper-grafo.
        """
        self.id = graph_id if graph_id else str(uuid.uuid4())
        self.name = name
        self.nodes: Dict[str, Node] = {}
        self.edges: Dict[str, Hyperedge] = {}
        
    def add_node(self, node: Node) -> None:
        """
        Adiciona um nó ao hiper-grafo.
        
        Args:
            node: Nó a ser adicionado.
        """
        self.nodes[node.id] = node
        
    def add_edge(self, edge: Hyperedge) -> None:
        """
        Adiciona uma hiper-aresta ao hiper-grafo.
        
        Args:
            edge: Hiper-aresta a ser adicionada.
        """
        # Verifica se todos os nós da hiper-aresta existem no grafo
        for node_id in edge.nodes:
            if node_id not in self.nodes:
                raise ValueError(f"Nó com ID {node_id} não existe no grafo.")
        
        self.edges[edge.id] = edge
        
    def get_node(self, node_id: str) -> Optional[Node]:
        """
        Obtém um nó pelo seu ID.
        
        Args:
            node_id: ID do nó a ser obtido.
            
        Returns:
            O nó correspondente ao ID, ou None se não existir.
        """
        return self.nodes.get(node_id)
    
    def get_edge(self, edge_id: str) -> Optional[Hyperedge]:
        """
        Obtém uma hiper-aresta pelo seu ID.
        
        Args:
            edge_id: ID da hiper-aresta a ser obtida.
            
        Returns:
            A hiper-aresta correspondente ao ID, ou None se não existir.
        """
        return self.edges.get(edge_id)
    
    def get_edges_for_node(self, node_id: str) -> List[Hyperedge]:
        """
        Obtém todas as hiper-arestas que contêm um determinado nó.
        
        Args:
            node_id: ID do nó.
            
        Returns:
            Lista de hiper-arestas que contêm o nó.
        """
        return [edge for edge in self.edges.values() if node_id in edge.nodes]
    
    def get_connected_nodes(self, node_id: str) -> Set[str]:
        """
        Obtém todos os nós conectados a um determinado nó através de hiper-arestas.
        
        Args:
            node_id: ID do nó.
            
        Returns:
            Conjunto de IDs dos nós conectados.
        """
        connected_nodes = set()
        for edge in self.get_edges_for_node(node_id):
            connected_nodes.update(edge.nodes)
        
        # Remove o próprio nó do conjunto
        if node_id in connected_nodes:
            connected_nodes.remove(node_id)
            
        return connected_nodes
    
    def remove_node(self, node_id: str) -> None:
        """
        Remove um nó do hiper-grafo e todas as hiper-arestas que o contêm.
        
        Args:
            node_id: ID do nó a ser removido.
        """
        if node_id in self.nodes:
            # Remove o nó
            del self.nodes[node_id]
            
            # Remove todas as hiper-arestas que contêm o nó
            edges_to_remove = [edge.id for edge in self.get_edges_for_node(node_id)]
            for edge_id in edges_to_remove:
                del self.edges[edge_id]
    
    def remove_edge(self, edge_id: str) -> None:
        """
        Remove uma hiper-aresta do hiper-grafo.
        
        Args:
            edge_id: ID da hiper-aresta a ser removida.
        """
        if edge_id in self.edges:
            del self.edges[edge_id]
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Converte o hiper-grafo para um dicionário.
        
        Returns:
            Um dicionário representando o hiper-grafo.
        """
        return {
            "id": self.id,
            "name": self.name,
            "nodes": [node.to_dict() for node in self.nodes.values()],
            "edges": [edge.to_dict() for edge in self.edges.values()]
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Hypergraph':
        """
        Cria um hiper-grafo a partir de um dicionário.
        
        Args:
            data: Dicionário contendo os dados do hiper-grafo.
            
        Returns:
            Uma instância de Hypergraph.
        """
        graph = cls(graph_id=data.get("id"), name=data.get("name", "Hypergraph"))
        
        # Adiciona os nós
        for node_data in data.get("nodes", []):
            node = Node.from_dict(node_data)
            graph.add_node(node)
        
        # Adiciona as hiper-arestas
        for edge_data in data.get("edges", []):
            edge = Hyperedge.from_dict(edge_data)
            # Ignora a verificação de nós existentes
            graph.edges[edge.id] = edge
        
        return graph
    
    def save_to_file(self, filepath: str) -> None:
        """
        Salva o hiper-grafo em um arquivo JSON.
        
        Args:
            filepath: Caminho do arquivo onde o hiper-grafo será salvo.
        """
        with open(filepath, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)
    
    @classmethod
    def load_from_file(cls, filepath: str) -> 'Hypergraph':
        """
        Carrega um hiper-grafo de um arquivo JSON.
        
        Args:
            filepath: Caminho do arquivo de onde o hiper-grafo será carregado.
            
        Returns:
            Uma instância de Hypergraph.
        """
        with open(filepath, 'r') as f:
            data = json.load(f)
        return cls.from_dict(data)
    
    def __str__(self) -> str:
        return f"{self.name}(id={self.id}, nodes={len(self.nodes)}, edges={len(self.edges)})"
    
    def __repr__(self) -> str:
        return self.__str__()

