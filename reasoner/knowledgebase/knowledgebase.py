import logging

logger=logging.getLogger(__name__)

class NodeSet(object):
    '''
        A set data structure for a node in the completion graph
    '''

    def __init__(self):
        self.axiom_set=set()
        logger.debug("Empty NodeSet initialised.")

    def add_axiom(self,axiom):
        '''
            Add a single axiom to the Set.
        '''
        if axiom not in self.axiom_set:
            logger.debug(f"Adding {axiom} to the KB")
            self.axiom_set.add(axiom)

    def add_axioms(self,axiom_list):
        '''
            Add multiple axioms to the Set.
        '''
        for axiom in axiom_list:
            self.add_axiom(axiom)

    def contains(self,axiom):
        '''
            Checks if the Set contains the given axiom.
        '''
        return axiom in self.axiom_set
