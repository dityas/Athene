import logging

logger=logging.getLogger(__name__)

from .nnf import NNF
from ..knowledgebase.axioms import *
from ..knowledgebase.graph import NodeSet,NodeNameGenerator

from copy import deepcopy

namer=NodeNameGenerator()

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
    #print(f"\r\nResolving {graph[node]} for {node}\r\n")
    axioms,expanded,consistent,edges=graph[node]
    while len(axioms["AND"]):
        axiom=axioms["AND"].pop()
        axiom1=axiom.term_a
        axiom2=axiom.term_b
        axioms,expanded,consistent=update_axioms(axiom1,axioms,expanded,consistent)
        axioms,expanded,consistent=update_axioms(axiom2,axioms,expanded,consistent)
        graph[node]=(axioms,expanded,consistent,edges)

    while len(axioms["OR"]):
        axiom=axioms["OR"].pop()
        axiom1=axiom.term_a
        axiom2=axiom.term_b
        graph_copy_a=deepcopy(graph)
        axioms_a,expanded_a,consistent_a,edges_a=graph_copy_a[node]
        graph_copy_b=deepcopy(graph)
        axioms_b,expanded_b,consistent_b,edges_b=graph_copy_b[node]
        (axioms_a,expanded_a,consistent_a)=update_axioms(axiom1,axioms_a,expanded_a,consistent_a)
        graph_copy_a[node]=(axioms_a,expanded_a,consistent_a,edges_a)
        models_a_copy=deepcopy(models)
        models_b_copy=deepcopy(models)
        models_a=run_expansion_loop(graph_copy_a,node,models_a_copy)
        if is_model_consistent(models_a):
            models+=models_a
        axioms_b,expanded_b,consistent_b=update_axioms(axiom2,axioms_b,expanded_b,consistent_b)
        graph_copy_b[node]=(axioms_b,expanded_b,consistent_b,edges_b)
        models_b=run_expansion_loop(graph_copy_b,node,models_b_copy)
        if is_model_consistent(models_b):
            models+=models_b
        return models

    while len(axioms["SOME"]):
        axiom=axioms["SOME"].pop()
        name=axiom.name
        axiom1=axiom.concept
        children=edges.setdefault(name)
        if children==None:
            node_name=namer.get_name()
            edges[name]=set({node_name})
            graph=prepare_graph(graph,node_name)
            axioms,expanded,consistent=update_axioms(axiom1,graph[node_name][0],graph[node_name][1],graph[node_name][2])
            graph[node_name]=(axioms,expanded,consistent,graph[node_name][3])
            return run_expansion_loop(graph,node_name,deepcopy(models))

        else:
            for child in children:
                axioms,expanded,consistent=update_axioms(axiom1,graph[child][0],graph[child][1],graph[child][2])
                graph[child]=(axioms,expanded,consistent,graph[child][3])
                models+=run_expansion_loop(graph,child,deepcopy(models))
            return models

    while len(axioms["ALL"]):
        axiom=axioms["ALL"].pop()
        name=axiom.name
        axiom1=axiom.concept
        children=edges.setdefault(name)
        if children != None:
            for child in children:
                axioms,expanded,consistent=update_axioms(axiom1,graph[child][0],graph[child][1],graph[child][2])
                graph[child]=(axioms,expanded,consistent,graph[child][3])
                models+=run_expansion_loop(graph,child,deepcopy(models))
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
        graph[individual]=(create_axioms_struct(),set(),True,{})
    return graph

def is_graph_consistent(graph):

    for node in graph.keys():
        if graph[node][2]==False:
            return False
    return True

def is_model_consistent(models):
    return len(list(filter(is_graph_consistent,models)))!=0

def prime_graph(graph,axiom,node):
    axioms=graph[node][0]
    expanded=graph[node][1]
    if axiom.type not in axioms.keys():
        expanded.add(axiom)
    else:
        axioms[axiom.type].add(axiom)
    return graph,axiom

def tree_search(models,node_list,node_index):
    if node_index==len(node_list):
        return models
    _models=[]
    for model in models:
        _models+=run_expansion_loop(model,node_list[node_index])
    return tree_search(_models,node_list,node_index+1)

def get_models(graph,axiom,individual):
    if individual=="#ALL":
        if len(graph)==0:
            graph=prepare_graph(graph,namer.get_name())
        for node in graph.keys():
            graph,axiom=prime_graph(graph,axiom,node)
        models=tree_search([graph],list(graph.keys()),0)
    else:
        graph=prepare_graph(graph,individual)
        graph,axiom=prime_graph(graph,axiom,individual)
        models=run_expansion_loop(graph,individual)

    return models

