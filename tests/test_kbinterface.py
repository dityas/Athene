import unittest
import sys 
import logging

#logging.basicConfig(level=logging.DEBUG)
sys.path.append("/home/adityas/Projects/ALC-reasoner/")

from reasoner.knowledgebase.knowledgebase import KnowledgeBase
from sample_axioms import *

class TestKBStructs(unittest.TestCase):

    def setUp(self):
        self.kb=KnowledgeBase()

    def test_run_sat_when_consistent(self):
        self.kb.load_from_list(consistent_complex_abox)
        self.kb.run_sat()
        self.assertTrue(self.kb.is_consistent())

    def test_run_sat_when_inconsistent(self):
        self.kb.load_from_list(inconsistent_complex_abox)
        self.kb.run_sat()
        self.assertFalse(self.kb.is_consistent())

    def test_check_sat_when_inconsistent(self):
        self.kb.load_from_list(consistent_complex_abox)
        self.kb.run_sat()
        self.assertFalse(self.kb.is_satisfiable(kinda_complicated_unsat_abox))

if __name__=="__main__":
    unittest.main()
