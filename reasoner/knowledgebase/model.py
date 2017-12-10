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

    def __split_class_assert(self,axiom):
        return axiom.definitions,axiom.instance.name

    def _get_sat_models(self,axiom,individual=None):
        models=[]
        for model in self.models:
            struct=search_model((model,[axiom],[],individual))
            models+=struct[2]
        return models

    def __process_graph(self,axiom,node=None):
        self.models=self._get_sat_models(axiom,node)

    def __consume_abox_axiom(self,axiom):
        logger.debug(f"Applying {axiom}")
        axiom,node=self.__split_class_assert(axiom)
        self.__process_graph(NNF(axiom),node)

    def is_consistent(self):
        return len(self.models)!=0

    def add_axiom(self,axiom):
        if axiom.type=="ABOX":
            axiom=axiom.axiom
            self.__consume_abox_axiom(axiom)
