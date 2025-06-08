class Node:
    def __init__(self, id, type, **kwargs):
        self.id = id
        self.type = type
        self.properties = kwargs

    def __repr__(self):
        return f"Node(id='{self.id}', type='{self.type}', properties={self.properties})"

class Hyperedge:
    def __init__(self, id, type, nodes, **kwargs):
        self.id = id
        self.type = type
        self.nodes = nodes  # List of node IDs involved in the hyperedge
        self.properties = kwargs

    def __repr__(self):
        return f"Hyperedge(id='{self.id}', type='{self.type}', nodes={self.nodes}, properties={self.properties})"

class Hypergraph:
    def __init__(self):
        self.nodes = {}
        self.hyperedges = {}

    def add_node(self, node):
        if not isinstance(node, Node):
            raise TypeError("Only Node objects can be added to the Hypergraph.")
        if node.id in self.nodes:
            raise ValueError(f"Node with ID '{node.id}' already exists.")
        self.nodes[node.id] = node

    def add_hyperedge(self, hyperedge):
        if not isinstance(hyperedge, Hyperedge):
            raise TypeError("Only Hyperedge objects can be added to the Hypergraph.")
        for node_id in hyperedge.nodes:
            if node_id not in self.nodes:
                raise ValueError(f"Node with ID '{node_id}' not found in the Hypergraph.")
        if hyperedge.id in self.hyperedges:
            raise ValueError(f"Hyperedge with ID '{hyperedge.id}' already exists.")
        self.hyperedges[hyperedge.id] = hyperedge

    def get_node(self, node_id):
        return self.nodes.get(node_id)

    def get_hyperedge(self, hyperedge_id):
        return self.hyperedges.get(hyperedge_id)

    def __repr__(self):
        return f"Hypergraph(nodes={len(self.nodes)}, hyperedges={len(self.hyperedges)})"


