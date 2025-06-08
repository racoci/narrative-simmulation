from .data_structures import Hypergraph, Node, Hyperedge

class Character:
    def __init__(self, id, archetype=None):
        self.id = id
        self.p_npc = Hypergraph()  # P_NPC is an instance of Hypergraph
        self._initialize_from_archetype(archetype)

    def _initialize_from_archetype(self, archetype):
        # This is a placeholder for archetype initialization logic.
        # In a real scenario, this would load predefined nodes and hyperedges
        # based on the archetype (e.g., 'hero', 'villain', 'commoner').
        if archetype:
            print(f"Initializing character {self.id} with archetype: {archetype}")
            # Example: Add a basic personality node
            if archetype == 'hero':
                self.p_npc.add_node(Node('p_courage', 'Personality', trait='Courage', value=0.8))
                self.p_npc.add_node(Node('v_justice', 'Value', valueName='Justice', priority=0.9))
            elif archetype == 'villain':
                self.p_npc.add_node(Node('p_selfishness', 'Personality', trait='Selfishness', value=0.9))
                self.p_npc.add_node(Node('v_power', 'Value', valueName='Power', priority=0.95))
            else:
                # Default nodes for any archetype if not specifically handled
                self.p_npc.add_node(Node('p_curiosity', 'Personality', trait='Curiosity', value=0.5))
                self.p_npc.add_node(Node('v_survival', 'Value', valueName='Survival', priority=0.7))

    def get_p_npc(self):
        return self.p_npc

    def __repr__(self):
        return f"Character(id=\'{self.id}\', p_npc={self.p_npc})"


