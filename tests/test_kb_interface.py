import unittest
import sys 
import logging

#logging.basicConfig(level=logging.DEBUG)
sys.path.append("/home/adityas/Projects/ALC-reasoner/")

from reasoner.knowledgebase.knowledgebase import KnowledgeBase
from sample_axioms import *

class TestKBInterface(unittest.TestCase):

    def setUp(self):
        self.KB=KnowledgeBase()

    def test_axiom_insertion(self):
        self.KB.load_from_list(consistent_complex_abox)
        self.assertTrue(self.KB.contains(consistent_complex_abox[1]))

    def test_consistency_when_consistent(self):
        self.KB.load_from_list(consistent_complex_abox)
        self.assertTrue(self.KB.is_consistent())

    def test_consistency_when_inconsistent(self):
        self.KB.load_from_list(inconsistent_complex_abox)
        self.assertFalse(self.KB.is_consistent())

    def test_sat_check_when_unsat(self):
        self.KB.load_from_list(consistent_complex_abox)
        self.assertTrue(self.KB.is_consistent())
        self.assertFalse(self.KB.is_satisfiable(kinda_complicated_unsat_abox))
        self.assertTrue(self.KB.is_consistent())

    def test_consistent_abox(self):
        self.KB.load_from_list(consistent_abox)
        self.assertTrue(self.KB.is_consistent())

if __name__=="__main__":
    unittest.main()
