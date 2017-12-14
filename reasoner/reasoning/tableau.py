import logging

logger=logging.getLogger(__name__)

from .nnf import NNF
from ..knowledgebase.axioms import *
from ..knowledgebase.graph import NodeSet

from copy import deepcopy

def update_and_check(label,label_set,consistency):
    if NNF(Not(label)) in label_set:
        consistency=False
    label_set.add(label)
    return label_set,consistency

def update_axioms(axiom,axiom_dict,label_set,consistent):
    if axiom.type in axiom_dict.keys():
        axiom_dict[axiom.type].add(axiom)
    else:
        label_set,consistent=update_and_check(axiom,label_set,consistent)

    return axiom_dict,label_set,consistent

def create_axioms_struct():
    return {"AND":set(),"OR":set(),"SOME":set(),"ALL":set()}

def run_expansion_loop(graph,node,models=None):
    '''
        Runs expansion rules according to tableau algorithm.
    '''
    if models==None:
        models=[]
    axioms,expanded,consistent=graph[node]
    while len(axioms["AND"]):
        axiom=axioms["AND"].pop()
        axiom1=axiom.term_a
        axiom2=axiom.term_b
        axioms,expanded,consistent=update_axioms(axiom1,axioms,expanded,consistent)
        axioms,expanded,consistent=update_axioms(axiom2,axioms,expanded,consistent)
        graph[node]=(axioms,expanded,consistent)

    while len(axioms["OR"]):
        axiom=axioms["OR"].pop()
        axiom1=axiom.term_a
        axiom2=axiom.term_b
        graph_copy=deepcopy(graph)
        graph_copy[node]=update_axioms(axiom1,deepcopy(axioms),deepcopy(expanded),consistent)
        models_a_copy=deepcopy(models)
        models_b_copy=deepcopy(models)
        models_a=run_expansion_loop(graph_copy,node,models_a_copy)
        if is_model_consistent(models_a):
            models+=models_a
        graph[node]=update_axioms(axiom2,axioms,expanded,consistent)
        models_b=run_expansion_loop(graph,node,models_b_copy)
        if is_model_consistent(models_b):
            models+=models_b
        return models

    if (len(axioms["AND"])==0) and (len(axioms["OR"])==0) and (len(axioms["SOME"])==0) and (len(axioms["ALL"])==0):
        if is_graph_consistent(graph):
            models.append(graph)
        return models
    else:
        return run_expansion_loop(graph,node,models)

def prepare_graph(graph,individual):
    '''
        Adds missing nodes, if any, and proceeds with the absorption of the
        axiom.
    '''
    node=graph.setdefault(individual)
    if node == None:
        graph[individual]=(create_axioms_struct(),set(),True)
    return graph

def is_graph_consistent(graph):

    for node in graph.keys():
        if graph[node][2]==False:
            return False
    return True

def is_model_consistent(models):
    return len(list(filter(is_graph_consistent,models)))!=0

def get_models(graph,axiom,individual):
    graph=prepare_graph(graph,individual)
    axioms=graph[individual][0]
    axioms[axiom.type].add(axiom)
    models=run_expansion_loop(graph,individual)
    return models

