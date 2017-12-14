import logging

logger=logging.getLogger(__name__)

import uuid
from .symbol_table import SymbolTable

table=SymbolTable()

def make_unique_id(name):
    '''
        Checks if symbol exists in the table. If it does, returns it else
        creates a new UUID.
    '''
    _uuid = table.get_uuid(name)
    if _uuid:
        logger.debug(f"{name} found in table.")
        return _uuid
    else:
        logger.debug(f"{name} does not exist. Making new entry.")
        _uuid=uuid.uuid1()
        table.add_to_table(name,str(_uuid))
        return _uuid

class Symbol(object):
    '''
        Used to define a single atom in an axiom. Should not be called
        explictly.
    '''
    def __init__(self,_string):
        self.label=_string
        self.id=make_unique_id(_string)

    def __eq__(self,other):
        """
            Overload equality operator to compare UUID instead of hashes.
        """
        return str(self.id)==other

    def __hash__(self):
        '''
            To help hashing axioms for storing in KB.
        '''
        return hash(self.id)

    def __repr__(self):
        return self.label

class Concept(Symbol):
    '''
        Define concept statements. 
        Returns a function.
        Concept assertion can be done by calling it with the atom as
        the argument.
    '''

    def __init__(self,name):
        super().__init__(name)
        self.name=name
        self.type="CONCEPT"
        logger.debug(f"Concept {name} initialised")

    def __str__(self):
        return str(self.name)

    def __hash__(self):
        return hash(str(self.id))

class Role(Symbol):
    
    def __init__(self,name,concept):
        super().__init__(name)
        self.name=name
        self.concept=concept

    def __str__(self):
        return self.type+"."+self.name+"."+str(self.concept)

class Some(Role):
    '''
        Defines Role statements.
    '''
    
    def __init__(self,name,concept):
        super().__init__(name,concept)
        self.type="SOME"

class All(Role):

    def __init__(self,name,concept):
        super().__init__(name,concept)
        self.type="ALL"

class Instance(Symbol):
    '''
        Defines individuals.
    '''

    def __init__(self,name):
        super().__init__(name)
        self.type="INSTANCE"
        self.name=name

    def __str__(self):
        return self.name
