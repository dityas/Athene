import logging

logger=logging.getLogger(__name__)

from .knowledgebase import NodeSet

class Node(object):
    '''
        Represents a single node in the completion graph. Used to represent a
        single instance in the concept assertion and then expanded from
        there.
    '''

    def __init__(self,
            individual,
            children={},
            expanded=NodeSet("expanded_axioms"),
            unexpanded=NodeSet("unexpanded_axioms"),
            labels=NodeSet("labels")):
            
        self.name=str(individual)
        self.expanded=expanded
        self.unexpanded=unexpanded
        self.labels=labels
        self.children=children
        logger.debug("Node {self.name} initialised.")
