import unittest
import sys 
import logging

#logging.basicConfig(level=logging.DEBUG)
sys.path.append("/home/adityas/Projects/ALC-reasoner/")

from reasoner.knowledgebase.model import Model
from sample_axioms import *

class TestModel(unittest.TestCase):

    def setUp(self):
        self.model=Model()

    def test_model_consistency_check(self):
        self.model.add_axiom(kinda_complicated_abox)
        self.assertTrue(self.model.is_consistent())
        
    def test_model_inconsistency_check(self):
        self.model.add_axiom(kinda_complicated_unsat_abox)
        self.assertFalse(self.model.is_consistent())

if __name__=="__main__":
    unittest.main()