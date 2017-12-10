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
        self.axiom_split_methods={"C_ASSERT":self.__split_class_assert,
                                "R_ASSERT":self.__split_role_assert}

    def __get_nnf(self,axiom):
        return NNF(axiom)

    def __split_class_assert(self,axiom):
        return axiom.definitions,axiom.instance.name

    def __split_role_assert(self,axiom):
        pass #TODO

    def _get_sat_models(self,axiom,individual=None):
        models=[]
        for model in self.models:
            struct=search_model((deepcopy(model),[axiom],[],individual))
            models+=struct[2]
        return models

    def __process_graph(self,axiom,node=None):
        self.models=self._get_sat_models(axiom,node)

    def __consume_abox_axiom(self,axiom):
        logger.debug(f"Applying {axiom}")
        axiom,node=self.axiom_split_methods[axiom.type](axiom)
        self.__process_graph(self.__get_nnf(axiom),node)

    def is_consistent(self):
        return len(self.models)!=0

    def is_satisfiable(self,axiom):
        _type=axiom.type
        if _type=="ABOX":
            axiom,node=self.axiom_split_methods[axiom.axiom.type](axiom.axiom)

        axiom=self.__get_nnf(axiom)
        return len(self._get_sat_models(axiom,node))!=0

    def add_axiom(self,axiom):
        if axiom.type=="ABOX":
            axiom=axiom.axiom
            self.__consume_abox_axiom(axiom)
