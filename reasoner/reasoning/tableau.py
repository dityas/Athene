import logging

logger=logging.getLogger(__name__)

from ..knowledgebase.axioms import And,Or,Not
from ..knowledgebase.graph import Graph
from ..common.constructors import Concept

def add_concept_to_node(graph,concept,node_name):
    '''
        Adds concept to node_name. If a node labelled node_name does not
        exist, it will be created.
    '''
    if not graph.contains(node_name):
        graph.make_node(name=node_name)
    graph.get_node(node_name).add_concept(concept)
    return graph

def make_model_copies(models_list):
    copy_list=[]
    for model in models_list:
        copy_list.append(Graph(**model.get_copy()))
    return copy_list

def search_model(model_struct):
    '''
        Performs DFS to search for a satisfiable model given the axiom.
        The struct is a tuple of the form (graph,axiom_list,final_states,node_name)
        initialised as (Graph(),[first_axiom],[],node_name)
    '''
    graph=model_struct[0]
    axiom_list=model_struct[1]
    known_models=model_struct[2]
    node_name=model_struct[3]
    print(f"Axioms to process {axiom_list}")

    if len(axiom_list):
        element=axiom_list.pop()
        print(f"Consuming axiom: {element}")
    else:
        if graph.is_consistent():
            print(f"Graph {graph} is consistent.")
            known_models.append(graph)
        else:
            print(f"Graph {graph} is inconsistent.")
        return (graph,axiom_list,known_models,node_name)

    axiom_type=type(element)

    if axiom_type==Concept or axiom_type==Not:
        graph=add_concept_to_node(graph,element,node_name)
        return search_model((graph,axiom_list,known_models,node_name))

    elif axiom_type==And:
        axiom_list.append(element.term_a)
        axiom_list.append(element.term_b)
        return search_model((graph,axiom_list,known_models,node_name))

    elif axiom_type==Or:

        axiomsA=axiom_list[:]
        axiomsB=axiom_list[:]
        axiomsA.append(element.term_a)
        axiomsB.append(element.term_b)
        known_copy=make_model_copies(known_models)
        graph_copy=Graph(**graph.get_copy())

        struct1=search_model((graph,axiomsA,known_models,node_name))
        print(f"Starting again with {graph_copy}")
        struct2=search_model((graph_copy,axiomsB,known_copy,node_name))
        if struct1[0].is_consistent():
            final_struct=(struct1[0],struct1[1],struct1[2]+struct2[2],struct1[3])
        else:
            final_struct=(struct2[0],struct2[1],struct1[2]+struct2[2],struct2[3])
        #return search_model(final_struct)
        return final_struct
