import unittest
import sys 
import logging

#logging.basicConfig(level=logging.DEBUG)
sys.path.append("/home/adityas/Projects/ALC-reasoner/")

from reasoner.common.constructors import Concept,Some,All

class TestConstructors(unittest.TestCase):

    def test_concept_constructor(self):
        self.assertEqual(Concept("Man").name,"Man")

    def test_some_role_constructor(self):
        some_role=Some("hasParent",Concept("Man"))
        self.assertEqual(some_role.name,"hasParent")
        self.assertEqual(some_role.concept.name,"Man")

    def test_all_constructor(self):
        all_role=All("hasParent",Concept("Man"))
        self.assertEqual(all_role.name,"hasParent")
        self.assertEqual(all_role.concept.name,"Man")

    def test_concept_equality(self):
        self.assertTrue(Concept("Man")==Concept("Man"))

    def test_concept_inequality(self):
        self.assertFalse(Concept("Man")==Concept("Woman"))

    def test_some_equality(self):
        self.assertEqual(Some("hasParent",Concept("Man")),Some("hasParent",Concept("Woman")))

    def test_all_equality(self):
        self.assertEqual(All("play",Concept("Child")),All("play",Concept("Man")))

if __name__=="__main__":
    unittest.main()
