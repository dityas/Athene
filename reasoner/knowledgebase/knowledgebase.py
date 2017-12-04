import logging

logger=logging.getLogger(__name__)

from .axioms import Assertion

class NodeSet(object):
    '''
        A set data structure for a node in the completion graph
    '''

    def __init__(self,name="Unnamed"):
        self.name=name
        self.axiom_set=set()
        logger.debug(f"Empty NodeSet {self.name} initialised.")

    def add_axiom(self,axiom):
        '''
            Add a single axiom to the Set.
        '''
        if axiom not in self.axiom_set:
            logger.debug(f"Adding {axiom} to the NodeSet {self.name}")
            self.axiom_set.add(axiom)

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
        if len(self.axiom_set):
            return self.axiom_set.pop()
        else:
            return None

    def contains(self,axiom):
        '''
            Checks if the Set contains the given axiom.
        '''
        logger.debug(f"Looking for {axiom} in {self.name}")
        return axiom in self.axiom_set

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
        for i,axiom in enumerate(self.axiom_set):
            logger.debug(f"{self.name} yielding axiom {axiom}")
            yield axiom

    def get_axioms(self):
        '''
            returns a list of all axioms in the box.
        '''
        return list(self.axiom_set)

class ABox(Box):
    '''
        Defines ABox.
    '''
    def __init__(self):
        super().__init__("abox")


class TBox(Box):
    '''
        Defines TBox.
    '''
    def __init__(self):
        super().__init__("tbox")


class KnowledgeBase(object):
    '''
        Defines the KB.
    '''

    def __init__(self):
        self.abox=ABox()
        self.tbox=TBox()
        logger.debug(f"Knowledge base initialised.")

    def __axiom_adder(self,axiom):
        if type(axiom)==Assertion:
            self.abox.add_axiom(axiom)
        else:
            self.tbox.add_axiom(axiom)

    def add_axioms(self,axiom_list):
        for axiom in axiom_list:
            self.__axiom_adder(axiom)

    def contains(self,axiom):
        '''
            returns whether the KB contains the given axiom.
        '''
        return self.abox.contains(axiom) or self.tbox.contains(axiom)


























