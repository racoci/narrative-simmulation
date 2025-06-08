import unittest
from src.modules.data_structures import Node, Hyperedge, Hypergraph
from src.modules.simulation_core import SimulationCore, Agent
from src.modules.world_module import World
from src.modules.character_module import Character
from src.modules.cognition_module import CognitionModule

class TestFase1And2(unittest.TestCase):

    def test_hypergraph_creation(self):
        hg = Hypergraph()
        self.assertIsInstance(hg, Hypergraph)
        self.assertEqual(len(hg.nodes), 0)
        self.assertEqual(len(hg.hyperedges), 0)

    def test_node_creation_and_addition(self):
        hg = Hypergraph()
        node1 = Node("n1", "Personality", trait="Honesty", value=0.7)
        hg.add_node(node1)
        self.assertEqual(hg.get_node("n1"), node1)
        self.assertEqual(hg.get_node("n1").properties["trait"], "Honesty")

    def test_hyperedge_creation_and_addition(self):
        hg = Hypergraph()
        node1 = Node("n1", "Personality", trait="Honesty", value=0.7)
        node2 = Node("n2", "Value", valueName="Security", priority=0.9)
        hg.add_node(node1)
        hg.add_node(node2)
        edge1 = Hyperedge("e1", "Memory", nodes=["n1", "n2"], emotionTag="Joy")
        hg.add_hyperedge(edge1)
        self.assertEqual(hg.get_hyperedge("e1"), edge1)
        self.assertEqual(hg.get_hyperedge("e1").properties["emotionTag"], "Joy")

    def test_simulation_core(self):
        sim_core = SimulationCore()
        self.assertIsInstance(sim_core, SimulationCore)
        self.assertEqual(sim_core.current_tick, 0)

        class TestAgent(Agent):
            def __init__(self, id):
                super().__init__(id)
                self.updated_ticks = []

            def update(self, current_tick):
                self.updated_ticks.append(current_tick)

        agent1 = TestAgent("agent1")
        sim_core.register_agent(agent1)
        sim_core.tick()
        self.assertEqual(sim_core.current_tick, 1)
        self.assertIn(1, agent1.updated_ticks)

    def test_world_module(self):
        world = World()
        self.assertIsInstance(world, World)
        world.add_entity("tree1", {"location": "forest", "age": 10})
        self.assertEqual(world.get_entity_properties("tree1")["age"], 10)
        world.update_entity_properties("tree1", {"age": 11})
        self.assertEqual(world.get_entity_properties("tree1")["age"], 11)
        world.remove_entity("tree1")
        self.assertIsNone(world.get_entity_properties("tree1"))

    def test_character_module(self):
        char1 = Character("char1", archetype="hero")
        self.assertIsInstance(char1, Character)
        self.assertIsInstance(char1.get_p_npc(), Hypergraph)
        self.assertIsNotNone(char1.get_p_npc().get_node("p_courage"))

    def test_cognition_module(self):
        char1 = Character("char1")
        cognition = CognitionModule(char1)
        self.assertIsInstance(cognition, CognitionModule)
        cognition.expanded_human_act()
        # Check if an EmotionEdge was added (simplified check)
        emotion_edge_found = False
        for edge_id, edge in char1.p_npc.hyperedges.items():
            if edge.type == "EmotionEdge":
                emotion_edge_found = True
                break
        self.assertTrue(emotion_edge_found)

if __name__ == '__main__':
    unittest.main()


