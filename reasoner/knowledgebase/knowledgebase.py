import logging

logger=logging.getLogger(__name__)

from .graph import NodeSet
from .model import Model

from copy import deepcopy
import pprint

class Box(NodeSet):
    '''
        Defines base object for ABox and TBox.
    '''

    def __init__(self,name):
        super().__init__(name=name)

    def extend(self,axioms):
        '''
            Adds a list of given axioms to the box.
        '''
        assert type(axioms)==list, "Argument for Box.extend has to be a list."
        self.add_axioms(axioms)

    def get_generator(self):
        '''
            returns a generator for getting axioms.
        '''
        for i,axiom in enumerate(self):
            logger.debug(f"{self.name} yielding axiom {axiom}")
            yield axiom

    def get_axioms(self):
        '''
            returns a list of all axioms in the box.
        '''
        return list(self)

class ABox(Box):
    '''
        Defines ABox.
    '''
    def __init__(self):
        super().__init__(name="abox")


class TBox(Box):
    '''
        Defines TBox.
    '''
    def __init__(self):
        super().__init__(name="tbox")


class KnowledgeBase(object):
    '''
        Defines the KB.
    '''

    def __init__(self):
        self.abox=ABox()
        self.tbox=TBox()
        self.model=Model()
        self.pp=pprint.PrettyPrinter(indent=2)
        logger.debug(f"Knowledge base initialised.")

    def __axiom_adder(self,axiom):
        '''
            Adds axiom to appropriate box.
        '''
        if axiom.type=="ABOX":
            self.abox.add_axiom(axiom)
        else:
            self.tbox.add_axiom(axiom)

    def init_axioms_list(self):
        '''
            Initialises self.axioms as a list of all axioms in the KB.
        '''
        self.axioms=self.abox.get_axioms()+self.tbox.get_axioms()

    def add_axioms(self,axiom_list):
        for axiom in axiom_list:
            self.__axiom_adder(axiom)

    def load_from_list(self,axioms):
        '''
            Loads axioms into KB from python lists.
        '''
        self.add_axioms(axioms)

    def contains(self,axiom):
        '''
            returns whether the KB contains the given axiom.
        '''
        return self.abox.contains(axiom) or self.tbox.contains(axiom)

    def is_consistent(self):
        return self.model.is_consistent()

    def is_satisfiable(self,axiom):
        return self.model.is_satisfiable(axiom)

    def run_sat(self):
        self.init_axioms_list()
        for axiom in self.axioms:
            self.model.add_axiom(axiom)

    def print_kb(self):
        self.init_axioms_list()
        self.pp.pprint(self.axioms)
