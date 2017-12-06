import unittest
import sys 
import logging

#logging.basicConfig(level=logging.DEBUG)
sys.path.append("/home/adityas/Projects/ALC-reasoner/")

from reasoner.common.constructors import Concept
from reasoner.knowledgebase.axioms import Not
from reasoner.knowledgebase.graph import Graph

from copy import deepcopy

class TestReasoning(unittest.TestCase):

    def setUp(self):
        self.graph=Graph()
        _=self.graph.make_node(name="Aditya")
        _=self.graph.make_node(name="Icarus")
        self.graph.make_node(name="Terminator")
        node=self.graph.get_node("Aditya")
        node.add_concept(Concept("Man"))
        node.add_concept(Concept("Sleepy"))
        node.add_concept(Concept("Symbolist"))
        anode=self.graph.get_node("Icarus")
        anode.add_concept(Concept("Man"))
        anode.add_concept(Concept("Machine"))

    def test_graph_inconsistency(self):
        node=self.graph.get_node("Icarus")
        node.add_concept(Not(Concept("Man")))
        self.assertFalse(self.graph.is_consistent())

    def test_graph_consistency(self):
        self.assertTrue(self.graph.is_consistent())

    def test_graph_printing(self):
        self.graph.make_edge("is","Aditya","Icarus")
        print(self.graph)
        another=self.graph.get_copy()
        another_graph=Graph(**another)
        node=another_graph.get_node("Terminator")
        node.add_concept(Concept("Machine"))
        print(another_graph)

if __name__=="__main__":
    unittest.main()
