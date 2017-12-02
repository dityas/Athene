import logging

logger=logging.getLogger(__name__)

class KnowledgeBase(object):

    def __init__(self):
        self.axioms=list()
        pass

    def add_axioms(self,axiom_list):
        for axiom in axiom_list:
            self.axioms.append(axiom)
