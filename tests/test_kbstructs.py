import unittest
import sys 
import logging

#logging.basicConfig(level=logging.DEBUG)
sys.path.append("/home/adityas/Projects/ALC-reasoner/")

from reasoner.knowledgebase.knowledgebase import NodeSet,KnowledgeBase
from reasoner.knowledgebase.axioms import And,Or,Not,Assertion
from reasoner.common.constructors import Concept,Some,All,Instance

class TestKBStructs(unittest.TestCase):

    def setUp(self):
        self.KB=NodeSet()
        self.axioms=[
            And(Concept("Man"),All("hasChild",Concept("Human"))),
            And(Concept("Woman"),All("hasChild",Concept("Human"))),
            Concept("Human"),
            Not(Concept("Robot"))
        ]
        self.KB.add_axioms(self.axioms)

    def test_add_multiple_axioms(self):
        self.assertEqual(len(self.KB),len(self.axioms))

    def test_add_single_axiom(self):
        self.KB.add_axiom(Concept("Terminator"))
        self.assertEqual(len(self.KB),len(self.axioms)+1)

    def test_contains_axiom(self):
        self.assertTrue(self.KB.contains(Concept("Human")))

    def test_not_contains_axiom(self):
        self.assertFalse(self.KB.contains(Concept("Dinosaur")))

if __name__=="__main__":
    unittest.main()
