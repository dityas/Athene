import unittest
import sys 
import logging

#logging.basicConfig(level=logging.DEBUG)
sys.path.append("/home/adityas/Projects/ALC-reasoner/")

from reasoner.knowledgebase.axioms import And,Or,Not,Assertion
from reasoner.common.constructors import Concept,All,Some,Instance

class TestAxioms(unittest.TestCase):

    def test_and_constructor(self):
        axiom=And(Concept("Man"),Some("hasChild",Concept("Human")))
        self.assertIsInstance(axiom,And)

    def test_or_constructor(self):
        axiom=Or(Concept("Man"),Concept("Woman"))
        self.assertIsInstance(axiom,Or)

    def test_not_constructor(self):
        axiom=Not(Concept("Human"))
        self.assertIsInstance(axiom,Not)

    def test_and_equality(self):
        axiom1=And(Concept("Man"),Concept("Woman"))
        axiom2=And(Concept("Man"),Concept("Woman"))
        axiom3=And(Concept("Woman"),Concept("Man"))
        self.assertEqual(axiom1,axiom2)
        self.assertEqual(axiom3,axiom1)

    def test_and_inequality(self):
        axiom1=And(Concept("Man"),Concept("Human"))
        axiom2=And(Concept("Woman"),Concept("Human"))
        self.assertNotEqual(axiom1,axiom2)

    def test_or_equality(self):
        axiom1=Or(Concept("Man"),Concept("Woman"))
        axiom2=Or(Concept("Man"),Concept("Woman"))
        axiom3=Or(Concept("Woman"),Concept("Man"))
        self.assertEqual(axiom1,axiom2)
        self.assertEqual(axiom3,axiom1)

    def test_or_inequality(self):
        axiom1=Or(Concept("Man"),Concept("Human"))
        axiom2=Or(Concept("Woman"),Concept("Human"))
        self.assertNotEqual(axiom1,axiom2)

    def test_not_equality(self):
        axiom1=Not(Concept("Man"))
        axiom2=Not(Concept("Man"))
        self.assertEqual(axiom2,axiom1)

    def test_not_inequality(self):
        axiom1=Not(Concept("Man"))
        axiom2=Not(Concept("Woman"))
        self.assertNotEqual(axiom1,axiom2)

    def test_assertion_constructor(self):
        instance=Instance("Aditya")
        _class=Concept("Man")
        axiom=Assertion(_class,instance)
        self.assertEqual(axiom.definitions,_class)
        self.assertEqual(axiom.instance,instance)

if __name__=="__main__":
    unittest.main()
