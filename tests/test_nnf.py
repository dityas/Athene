import unittest
import sys 
import logging

#logging.basicConfig(level=logging.DEBUG)
sys.path.append("/home/adityas/Projects/ALC-reasoner/")

from reasoner.knowledgebase.knowledgebase import NodeSet
from reasoner.knowledgebase.axioms import And,Or,Not
from reasoner.common.constructors import Concept,Some,All
from reasoner.reasoning.nnf import NNF

class TestNNF(unittest.TestCase):

    def test_nnf_concept(self):
        self.assertEqual(Concept("A"),NNF(Concept("A")))

    def test_nnf_not_concept(self):
        self.assertEqual(Not(Concept("A")),NNF(Not(Concept("A"))))

    def test_nnf_not_not_concept(self):
        self.assertEqual(NNF(Not(Not(Concept("A")))),Concept("A"))

    def test_nnf_not_not_not_concept(self):
        self.assertEqual(NNF(Not(Not(Not(Concept("A"))))),Not(Concept("A")))
        self.assertNotEqual(Not(Not(Concept("A"))),Not(Concept("A")))

    def test_nnf_or(self):
        axiom1=Or(Concept("A"),Concept("B"))
        axiom2=Or(Concept("A"),Not(Concept("B")))
        axiom3=Or(Not(Not(Concept("A"))),Not(Not(Concept("B"))))
        self.assertEqual(axiom1,NNF(axiom1))
        self.assertEqual(axiom1,NNF(axiom3))
        self.assertNotEqual(axiom1,NNF(axiom2))

    def test_nnf_not_or(self):
        axiom1=Not(Or(Concept("A"),Concept("B")))
        axiom2=And(Not(Concept("A")),Not(Concept("B")))
        self.assertEqual(axiom2,NNF(axiom1))

    def test_nnf_and(self):
        axiom1=And(Concept("A"),Concept("B"))
        axiom2=And(Not(Not(Concept("A"))),Not(Not(Concept("B"))))
        self.assertEqual(axiom1,NNF(axiom2))

    def test_nnf_not_and(self):
        axiom1=Not(And(Concept("A"),Concept("B")))
        axiom2=Or(Not(Concept("A")),Not(Concept("B")))
        self.assertEqual(axiom2,NNF(axiom1))

    def test_nnf_some(self):
        axiom1=Some("A",Concept("B"))
        self.assertEqual(axiom1,NNF(axiom1))

    def test_nnf_not_some(self):
        axiom1=Not(Some("A",Concept("B")))
        axiom2=All("A",Not(Concept("B")))
        self.assertEqual(NNF(axiom1),axiom2)

    def test_nnf_all(self):
        axiom1=All("A",Concept("B"))
        self.assertEqual(NNF(axiom1),axiom1)

    def test_nnf_not_all(self):
        axiom1=Not(All("A",Concept("B")))
        axiom2=Some("A",Not(Concept("B")))
        self.assertEqual(NNF(axiom1),axiom2)

    def test_nnf_complex_statement(self):
        axiom1=Not(And(Some("A",Concept("B")),Not(Concept("C"))))
        axiom2=Or(All("A",Not(Concept("B"))),Concept("C"))
        self.assertEqual(axiom2,NNF(axiom1))

if __name__=="__main__":
    unittest.main()
