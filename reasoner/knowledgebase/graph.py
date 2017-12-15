import logging

logger=logging.getLogger(__name__)

from .axioms import Not
from ..common.constructors import Concept
from ..reasoning.nnf import NNF

from copy import deepcopy

class NodeSet(set):
    '''
        A set data structure for a node in the completion graph
    '''

    def __init__(self,obj=None,name="Unnamed"):
        if obj:
            super().__init__(obj)
        self.name=name
        logger.debug(f"Empty NodeSet {self.name} initialised.")

    def add_axiom(self,axiom):
        '''
            Add a single axiom to the Set.
        '''
        if axiom not in self:
            logger.debug(f"Adding {axiom} to the NodeSet {self.name}")
            self.add(axiom)

    def add_axioms(self,axiom_list):
        '''
            Add multiple axioms to the Set.
        '''
        for axiom in axiom_list:
            self.add_axiom(axiom)

    def pop_axiom(self):
        '''
            Remove and return an axiom from the set of all axioms.
        '''
        if len(self):
            return self.pop()
        else:
            return None

    def contains(self,axiom):
        '''
            Checks if the Set contains the given axiom.
        '''
        logger.debug(f"Looking for {axiom} in {self.name}")
        return axiom in self

    def __deepcopy__(self,memo):
        return NodeSet(deepcopy(set(self)))


class NodeNameGenerator(object):
    '''
        Used for naming unnamed nodes.
    '''
    def __init__(self):
        self.i=0

    def get_name(self):
        name="no_name:"+str(self.i)
        self.i+=1
        return name

