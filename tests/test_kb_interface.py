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
        self.assertTrue(consistent_complex_abox[2])

if __name__=="__main__":
    unittest.main()
