import logging

logger=logging.getLogger(__name__)

from .model import Model

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
        self.axioms=self.tbox.get_axioms+self.abox.get_axioms

    def add_axioms(self,axiom_list):
        for axiom in axiom_list:
            self.__axiom_adder(axiom)

    def load_from_list(self,axioms):
        '''
            Loads axioms into KB from python lists.
        '''
        self.add_axioms(axioms)

    def run_model(self):
        '''
            Create a model for the current axioms in the KB.
        '''
        self.init_axioms_list()
        for axiom in self.axioms:
            model.add_axiom(axiom)

    def is_consistent(self):
        return self.model.is_consistent()

    def is_satisfiable(self,axiom):
        return self.model.is_satisfiable(axiom)

    def contains(self,axiom):
        '''
            returns whether the KB contains the given axiom.
        '''
        return self.abox.contains(axiom) or self.tbox.contains(axiom)
