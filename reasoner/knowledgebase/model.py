import logging

logger=logging.getLogger(__name__)

from .graph import Graph

class Model(object):
    '''
        Represents a model in the tableau. Contains multiple graphs based on
        non determinism.
    '''

    def __init__(self):
        pass
