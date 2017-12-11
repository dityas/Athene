import logging

logger=logging.getLogger(__name__)

from .axioms import Not
from ..common.constructors import Concept
from ..reasoning.nnf import NNF

from copy import deepcopy

class NodeSet(set):
    '''
        A set data structure for a node in the completion graph
    '''

    def __init__(self,obj=None,name="Unnamed"):
        if obj:
            super().__init__(obj)
        self.name=name
        logger.debug(f"Empty NodeSet {self.name} initialised.")

    def add_axiom(self,axiom):
        '''
            Add a single axiom to the Set.
        '''
        if axiom not in self:
            logger.debug(f"Adding {axiom} to the NodeSet {self.name}")
            self.add(axiom)

    def add_axioms(self,axiom_list):
        '''
            Add multiple axioms to the Set.
        '''
        for axiom in axiom_list:
            self.add_axiom(axiom)

    def pop_axiom(self):
        '''
            Remove and return an axiom from the set of all axioms.
        '''
        if len(self):
            return self.pop()
        else:
            return None

    def contains(self,axiom):
        '''
            Checks if the Set contains the given axiom.
        '''
        logger.debug(f"Looking for {axiom} in {self.name}")
        return axiom in self

    def __deepcopy__(self,memo):
        return NodeSet(deepcopy(set(self)))


class NodeNameGenerator(object):
    '''
        Used for naming unnamed nodes.
    '''
    def __init__(self):
        self.i=0

    def get_name(self):
        name="no_name:"+str(self.i)
        self.i+=1
        return name

class Node(object):
    '''
        Represents a single node in the completion graph. Used to represent a
        single instance in the concept assertion and then expanded from
        there.
    '''

    def __init__(self,
            name=None,
            labels=None,
            children=None,
            consistent=True):

        if labels == None:
            self.name=name
            self.labels=NodeSet(name="labels")
            self.children={}
            self.CONSISTENT=True
        else:
            self.name=name
            self.labels=labels
            self.children=children
            self.CONSISTENT=consistent
        logger.debug(f"Node {self.name} initialised.")

    def add_concept(self,concept):
        '''
            Adds a concept label to the node. label will be checked for a
            clash before addition.
        '''
        if NNF(Not(concept)) in self.labels:
            logger.info(f"Inconsistency in {self.name} while adding {concept}")
            self.CONSISTENT=False
        if NNF(concept) not in self.labels:
            self.labels.add_axiom(concept)

    def set_consistency_marker(self):
        '''
            Set consistency flag to True after satisfiability check.
        '''
        self.CONSISTENT=True
        logger.critical(f"Manually setting consistency on {self.name}.")

    def contains(self,axiom):
        return self.labels.contains(axiom)

    def __eq__(self,other):
        return self.name==other

    def __repr__(self):
        a=f"---{self.name}---\r\nLABELS:{self.labels}\r\nCHILDREN:{self.children}\r\nCONSISTENT:{self.CONSISTENT}"
        return a

    def __deepcopy__(self,memo):
        return Node(name=self.name,
                labels=deepcopy(self.labels),
                children=self.children.copy(),
                consistent=self.CONSISTENT)

class Graph(object):
    '''
        Represents a completion graph of nodes.
    '''

    def __init__(self,nodes=None,edges=None):
        self.namer=NodeNameGenerator()
        if nodes==None:
            self.nodes={}
        else:
            self.nodes=nodes
        if edges==None:
            self.edges={}
        else:
            self.edges=edges
        logger.debug(f"Initialised empty graph {self}.")

    def make_node(self,node=None,name=None):
        '''
            If the node to be generated is given, generate that node. Else
            generate a new node with the given name or a random name. Returns
            the name of the node.
        '''
        if node:
            name=node.name
            self.nodes[name]=node
        else:
            if name==None:
                name=self.namer.get_name()
            self.nodes[name]=Node(name=name)
        logger.debug(f"made new node {name} in {self}")
        return name

    def make_edge(self,name,parent,child):
        '''
            Make an edge with label name from parent to child.
        '''
        parents=self.edges.setdefault(name)
        if parents!=None:
            parents.add(parent)
        else:
            self.edges[name]=set([parent])
        children_dict=self.nodes[parent].children
        children=children_dict.setdefault(name)
        if children==None:
            children_dict[name]=set([child])
        else:
            children.add(child)
        logger.debug(f"made edge {name} from {parent} to {child} in {self}")

    def edge_exists(self,parent,name,child):
        '''
            Returns true if an edge exists between given parent and child.
        '''
        parent=self.nodes[parent]
        children=parent.children.setdefault(name)
        if children != None and (child in children):
            return True
        else:
            return False

    def get_connected_children(self,parent,edge_name):
        '''
            returns a list of connected nodes to a parent node along the
            given edge.
        '''
        node=self.get_node(name=parent)
        children=node.children.setdefault(edge_name)
        if children==None:
            return []
        else:
            return list(map(lambda x:self.get_node(name=x),list(children)))


    def contains(self,name):
        node=self.nodes.setdefault(name)
        return node!=None

    def get_node(self,name):
        '''
            Returns reference of the node corrosponding to the given name.
        '''
        if self.contains(name):
            return self.nodes[name]
        else:
            return None

    def is_consistent(self):
        return len(list(filter(lambda y:y==False,map(lambda x:x[1].CONSISTENT,list(self.nodes.items())))))==0

    def mark_consistent(self):
        '''
            Marks all nodes in the graph as consistent.
        '''
        for key in self.nodes.keys():
            self.nodes[key].set_consistency_marker()

    def __deepcopy__(self,memo):
        '''
            Returns a copy of the nodes and edges to help create an identical
            copy of the graph outside.
        '''
        return Graph(nodes=deepcopy(self.nodes),
                    edges=self.edges.copy())

    def __repr__(self):
        r=f"\r\n---GRAPH---\r\nNODES:{self.nodes}\r\nEDGES:{self.edges}\r\n-----------\r\n"
        return r
