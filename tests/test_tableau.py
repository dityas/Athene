import unittest
import sys 
import logging

#logging.basicConfig(level=logging.DEBUG)
sys.path.append("/home/adityas/Projects/ALC-reasoner/")

from reasoner.knowledgebase.axioms import And,Or,Not,ClassAssertion,RoleAssertion,TBoxAxiom,Subsumption
from reasoner.common.constructors import Concept,All,Some,Instance
from reasoner.reasoning.tableau import *

class TestTableau(unittest.TestCase):

    def test_simple_and(self):
        axiom=And(And(Concept("Man"),Concept("Living")),And(Concept("Machine"),Concept("Terminator")))
        models=get_models({},axiom,"Aditya")
        self.assertTrue(is_model_consistent(models))

    def test_unsat_and(self):
        axiom=And(And(Concept("Man"),Concept("Living")),And(Not(Concept("Man")),Concept("Terminator")))
        models=get_models({},axiom,"Aditya")
        self.assertFalse(is_model_consistent(models))

    def test_simple_or(self):
        axiom=Or(Concept("Man"),Concept("Terminator"))
        models=get_models({},axiom,"Aditya")
        self.assertTrue(is_model_consistent(models))

    def test_complex_and_or(self):
        axiom=Or(And(Or(Not(Concept("Machine")),Concept("Machine")),Concept("Machine")),And(Or(Not(Concept("Man")),Concept("Man")),Concept("Man")))
        models=get_models({},axiom,"Aditya")
        self.assertTrue(is_model_consistent(models))

if __name__=="__main__":
    unittest.main()
