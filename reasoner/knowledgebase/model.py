import logging

logger=logging.getLogger(__name__)

from .graph import Graph
from ..reasoning.nnf import NNF
from ..reasoning.tableau import search_model

from copy import deepcopy

class Model(object):
    '''
        Represents a set of satisfiable models for the given axioms.
    '''

    def __init__(self):
        self.models=[Graph()]

    def __get_nnf(self,axiom):
        return NNF(axiom)

    def _get_sat_models(self,axiom,individual=None):
        models=[]
        for model in self.models:
            struct=search_model((model,[axiom],[],individual))
            models+=struct[2]
        return models

    def __consume_abox_axiom(self,axiom,individual):
        logger.debug(f"Applying {axiom} to node {individual}")
        axiom=self.__get_nnf(axiom)
        self.models=self._get_sat_models(axiom,individual)

    def is_consistent(self):
        return len(self.models)!=0

    def add_axiom(self,axiom):
        if axiom.type=="ABOX":
            axiom=axiom.axiom
            self.__consume_abox_axiom(axiom.definitions,axiom.instance.name)
