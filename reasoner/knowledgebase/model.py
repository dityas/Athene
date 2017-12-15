import logging

logger=logging.getLogger(__name__)

from ..reasoning.nnf import NNF
from ..reasoning.tableau import get_models

from copy import deepcopy
import pprint

class Model(object):
    '''
        Represents a set of satisfiable models for the given axioms.
    '''

    def __init__(self):
        self.models=[{}]
        self.pp=pprint.PrettyPrinter(indent=2)
        self.axiom_split_methods={"C_ASSERT":self.__split_class_assert,
                                "R_ASSERT":self.__split_role_assert}

    def __get_nnf(self,axiom):
        return NNF(axiom)

    def __split_class_assert(self,axiom):
        return axiom.definitions,axiom.instance.name

    def __split_role_assert(self,axiom):
        return axiom,(axiom.instance1.name,axiom.instance2.name)

    def _get_sat_models(self,axiom,individual=None):
        '''
            Runs tableau on a copy of currently satisfiable models and
            returns satisfiable ones.
        '''
        models=[]
        for model in self.models:
            models+=get_models(model,axiom,individual)
        return models

    def __process_graph(self,axiom,node=None):
        '''
            Commits changes in satisfiable graphs.
        '''
        self.models=self._get_sat_models(axiom,node)

    def __consume_abox_axiom(self,axiom):
        '''
            Permanently adds ABOX axiom to the graph.
        '''
        logger.debug(f"Applying {axiom}")
        axiom,node=self.axiom_split_methods[axiom.type](axiom)
        self.__process_graph(self.__get_nnf(axiom),node)

    def __consume_tbox_axiom(self,axiom):
        '''
            Permanently adds TBOX axiom to the graph.
        '''
        logger.debug(f"Applying TBOX axiom {axiom}")
        self.__process_graph(self.__get_nnf(axiom),"#ALL")

    def is_consistent(self):
        return len(self.models)!=0

    def is_satisfiable(self,axiom):
        '''
            Checks if given axiom is satisfiale for the currently satisfiable
            models. Any changes made during inference are discarded.
        '''
        _type=axiom.type
        if _type=="ABOX":
            axiom,node=self.axiom_split_methods[axiom.axiom.type](axiom.axiom)

        axiom=self.__get_nnf(axiom)
        return len(self._get_sat_models(axiom,node))!=0

    def add_axiom(self,axiom):
        '''
            Permanently adds given axiom to the graph.
        '''
        if axiom.type=="ABOX":
            axiom=axiom.axiom
            self.__consume_abox_axiom(axiom)

        elif axiom.type=="TBOX":
            axiom=axiom.axiom
            self.__consume_tbox_axiom(axiom)

    def debug_print(self):
        self.pp.pprint(self.models)
