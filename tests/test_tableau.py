import unittest
import sys 
import logging

#logging.basicConfig(level=logging.DEBUG)
sys.path.append("/home/adityas/Projects/ALC-reasoner/")

#from reasoner.knowledgebase.knowledgebase import NodeSet,KnowledgeBase
from reasoner.knowledgebase.axioms import And,Or,Not,ClassAssertion
from reasoner.knowledgebase.graph import Graph
from reasoner.common.constructors import Concept,Some,All,Instance
from reasoner.reasoning.tableau import *
from sample_axioms import complex_or,simple_or,kinda_complicated_axiom

class TestTableau(unittest.TestCase):

    def setUp(self):
        self.graph=Graph()
        self.and_axiom=And(And(Concept("Man"),Concept("Student")),Not(Concept("Robot")))
        self.simple_some=Some("hasComputer",Not(Concept("HAL")))

    def test_termination(self):
        struct=search_model((self.graph,[Concept("Man")],[],"Aditya"))
        self.assertEqual(len(struct[2]),1)

    def test_and_handling(self):
        struct=search_model((self.graph,[self.and_axiom],[],"Aditya"))
        sat_model=struct[2][0]
        self.assertEqual(len(struct[1]),0)
        node=sat_model.get_node("Aditya")
        labels=node.labels
        self.assertTrue(len(labels)==3)

    def test_or_handling(self):
        struct=search_model((self.graph,[simple_or],[],"Aditya"))
        self.assertEqual(len(struct[2]),2)

    def test_complex_or_handling(self):
        struct=search_model((self.graph,[complex_or],[],"Aditya"))
        self.assertEqual(len(struct[2]),3)

    def test_complicated_axiom(self):
        struct=search_model((self.graph,[kinda_complicated_axiom],[],"Aditya"))
        self.assertEqual(len(struct[2]),2)

    def test_some_role_assertion(self):
        struct=search_model((self.graph,[self.simple_some],[],"Aditya"))
        self.assertEqual(len(struct[0].nodes),2)

    def test_some_when_exists(self):
        struct=search_model((self.graph,[self.and_axiom],[],"Aditya"))
        self.assertEqual(len(struct[0].nodes),1)
        struct=search_model((struct[0],[self.simple_some],struct[2],"Aditya"))
        self.assertEqual(len(struct[0].nodes),2)
        struct=search_model((struct[0],[self.simple_some],struct[2],"Aditya"))
        self.assertEqual(len(struct[0].nodes),2)

    def test_some_when_node_exists(self):
        struct=search_model((self.graph,[self.and_axiom],[],"Aditya"))
        self.assertEqual(len(struct[0].nodes),1)
        struct=search_model((struct[0],[self.simple_some],struct[2],"Aditya"))
        self.assertEqual(len(struct[0].nodes),2)
        struct=search_model((struct[0],[Some("hasComputer",Not(Concept("Jarvis")))],struct[2],"Aditya"))
        self.assertEqual(len(struct[0].nodes),3)

    def test_all_when_node_exists(self):
        struct=search_model((self.graph,[self.and_axiom],[],"Aditya"))
        self.assertEqual(len(struct[0].nodes),1)
        struct=search_model((struct[0],[self.simple_some],struct[2],"Aditya"))
        self.assertEqual(len(struct[0].nodes),2)
        struct=search_model((struct[0],[All("hasComputer",Not(Concept("Jarvis")))],struct[2],"Aditya"))
        self.assertEqual(len(struct[0].nodes),2)

if __name__=="__main__":
    unittest.main()
