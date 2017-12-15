import unittest
import sys 
import logging

#logging.basicConfig(level=logging.DEBUG)
sys.path.append("/home/adityas/Projects/ALC-reasoner/")

from reasoner.knowledgebase.knowledgebase import KnowledgeBase
from sample_kb import *

class TestWithOntology(unittest.TestCase):

    def setUp(self):
        self.kb=KnowledgeBase()

    def test_small_kb(self):
        self.kb.load_from_list(small_kb)
        self.kb.run_sat()
        print("KB is.")
        self.kb.print_kb()
        print("Computed models are.")
        self.kb.model.debug_print()

    def test_little_kb(self):
        self.kb.load_from_list(little_kb)
        self.kb.run_sat()
        print("KB is.")
        self.kb.print_kb()
        print("Computed models are.")
        self.kb.model.debug_print()

    def test_simple_kb(self):
        self.kb.load_from_list(simple_kb)
        self.kb.run_sat()
        print("KB is.")
        self.kb.print_kb()
        print("Computed models are.")
        self.kb.model.debug_print()

    def test_inconsistent_kb(self):
        self.kb.load_from_list(inconsistent_test_kb)
        self.kb.run_sat()
        print("KB is.")
        self.kb.print_kb()
        print("Computed models are.")
        self.kb.model.debug_print()

    def test_another_kb(self):
        self.kb.load_from_list(yet_another_kb)
        self.kb.run_sat()
        print("KB is.")
        self.kb.print_kb()
        print("Computed models are.")
        self.kb.model.debug_print()

if __name__=="__main__":
    unittest.main()
