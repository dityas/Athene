import unittest
import sys 
import logging

#logging.basicConfig(level=logging.DEBUG)
sys.path.append("/home/adityas/Projects/ALC-reasoner/")

from reasoner.common.symbol_table import SymbolTable

class TestSymbolTable(unittest.TestCase):

    def setUp(self):
        self.table=SymbolTable()

    def test_add_to_table(self):
        self.table.add_to_table("foo","bar")
        self.assertEqual(len(self.table.uuid_to_name),1)
        self.assertEqual(len(self.table.name_to_uuid),1)

    def test_get_name(self):
        self.table.add_to_table("foo","bar")
        name=self.table.get_name("bar")
        self.assertEqual(name,"foo")

    def test_get_name_not_present(self):
        self.table.add_to_table("foo","bar")
        name=self.table.get_name("bullshit")
        self.assertIsNone(name)

    def test_get_uuid(self):
        self.table.add_to_table("foo","bar")
        uuid=self.table.get_uuid("foo")
        self.assertEqual(uuid,"bar")

    def test_get_uuid_not_present(self):
        self.table.add_to_table("foo","bar")
        self.assertIsNone(self.table.get_uuid("bullshit"))

if __name__=="__main__":
    unittest.main()
