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

    def __init__(self,model_struct=None):
        if model_struct:
            self.model_struct=model_struct
        else:
            self.model_struct=(Graph(),[],[],None)

    def __get_nnf(self,axiom):
        return NNF(axiom)

    def __add_axiom_to_struct(self,axiom):
        graph,axioms,models,node=self.model_struct
        axioms.append(axiom)
        self.model_struct=(graph,axioms,models,node)
        logger.debug(f"Changed model_struct to {self.model_struct}")

    def __add_individual_to_struct(self,individual):
        graph,axioms,models,node=self.model_struct
        self.model_struct=(graph,axioms,models,individual)
        logger.debug(f"Changed model_struct to {self.model_struct}")

    def __consume_abox_axiom(self,axiom,individual):
        logger.debug(f"Applying {axiom} to node {individual}")
        axiom=self.__get_nnf(axiom)
        self.__add_axiom_to_struct(axiom)
        self.__add_individual_to_struct(individual)
        self.model_struct=search_model(self.model_struct)

    def _get_satisfiable_models(self):
        models=self.model_struct[2]
        return list(filter(lambda x:x.is_consistent(),models))

    def is_consistent(self):
        sat_models=self._get_satisfiable_models()
        return len(sat_models)!=0

    def is_satisfiable(self,axiom):
        '''
            Returns True is models satisfy the given axiom without actually
            adding the axiom.
        '''
        graph,axioms,models,node=self.model_struct
        backup=(deepcopy(graph),axioms[:],models[:],node)
        self.add_axiom(axiom)
        satisfiability=self.is_consistent()
        self.model_struct=backup
        return satisfiability

    def add_axiom(self,axiom):
        if axiom.type=="ABOX":
            axiom=axiom.axiom
            self.__consume_abox_axiom(axiom.definitions,axiom.instance.name)
