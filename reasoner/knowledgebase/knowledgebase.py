import logging

logger=logging.getLogger(__name__)

class NodeSet(object):
    '''
        A set data structure for a node in the completion graph
    '''

    def __init__(self,name="Unnamed"):
        self.name=name
        self.axiom_set=set()
        logger.debug("Empty NodeSet initialised.")

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
        return axiom in self.axiom_set
