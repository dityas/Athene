import logging

logger=logging.getLogger(__name__)

class KnowledgeBase(object):
    '''
        Data structure for the knowledge base
    '''

    def __init__(self):
        self.axiom_set=set()
        logger.debug("Empty KB initialised.")

    def add_axiom(self,axiom):
        '''
            Add a single axiom to the KB.
        '''
        if axiom not in self.axiom_set:
            logger.debug(f"Adding {axiom} to the KB")
            self.axiom_set.add(axiom)

    def add_axioms(self,axiom_list):
        '''
            Add multiple axioms to the KB.
        '''
        for axiom in axiom_list:
            self.add_axiom(axiom)

    def contains(self,axiom):
        '''
            Checks if the KB contains the given axiom.
        '''
        return axiom in self.axiom_set
