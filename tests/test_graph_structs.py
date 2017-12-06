import unittest
import sys 
import logging

#logging.basicCenfig(level=logging.DEBUG)
sys.path.append("/home/adityas/Projects/ALC-reasoner/")

from reasoner.common.constructors import Concept
from reasoner.knowledgebase.axioms import Not
from reasoner.knowledgebase.graph import NodeNameGenerator,Node,Graph

class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph=Graph()

    def test_node_creation(self):
        self.graph.make_node(name="Aditya")
        self.assertTrue(self.graph.contains("Aditya"))

    def test_unnamed_node_creation(self):
        name=self.graph.make_node()
        self.assertTrue(self.graph.contains(name))

    def test_edge_creation(self):
        self.graph.make_node(name="Aditya")
        self.graph.make_node(name="Icarus")
        self.graph.make_edge("is","Aditya","Icarus")
        self.assertTrue("is" in self.graph.edges.keys())

    def test_edge_exists(self):
        self.graph.make_node(name="Aditya")
        self.graph.make_node(name="Icarus")
        self.graph.make_edge("is","Aditya","Icarus")
        self.assertTrue(self.graph.edge_exists("Aditya","is","Icarus"))

    def test_get_node(self):
        self.graph.make_node(name="Aditya")
        node=self.graph.get_node("Aditya")
        self.assertEqual(node.name,"Aditya")

    def test_get_connected_children(self):
        self.graph.make_node(name="A")
        self.graph.make_node(name="B")
        name=self.graph.make_node()
        self.graph.make_edge("role","A","B")
        self.graph.make_edge("role","A",name)
        self.assertEqual(len(self.graph.get_connected_children("A","role")),2)

class TestNode(unittest.TestCase):

    def setUp(self):
        self.node=Node("Icarus")

    def test_concept_addition(self):
        self.node.add_concept(Concept("Man"))
        self.assertTrue(self.node.CONSISTENT)
        self.assertTrue(self.node.labels.contains(Concept("Man")))

    def test_consistency_check(self):
        self.node.add_concept(Concept("Man"))
        self.node.add_concept(Not(Concept("Man")))
        self.assertFalse(self.node.CONSISTENT)

    def test_set_consistency_marker(self):
        self.node.add_concept(Concept("Man"))
        self.node.add_concept(Not(Concept("Man")))
        self.assertFalse(self.node.CONSISTENT)
        self.node.set_consistency_marker()
        self.assertTrue(self.node.CONSISTENT)

if __name__=="__main__":
    unittest.main()
