import logging

logger=logging.getLogger(__name__)

class Axiom(object):
    '''
        Base class in case some common methods have to be written. Should not
        be called explicitly.
    '''

    def __init__(self,_type):
        self.type=_type

class And(Axiom):
    '''
        Class for writing And axioms. 
        Ex. A ^ B is written as And(A,B)
    '''

    def __init__(self,term_a,term_b):
        super().__init__("AND")
        self.term_a=term_a
        self.term_b=term_b
        logger.debug(f"Initialised axiom And({self.term_a},{self.term_b})")

    def __eq__(self,other):
        params=(self.type,self.term_a,self.term_b)
        params_inv=(self.type,self.term_b,self.term_a)
        return (params == other) or (params_inv == other)

    def __hash__(self):
        return hash(self.type+str(hash(self.term_a))+str(hash(self.term_b)))

    def __str__(self):
        return "("+str(self.term_a)+" AND "+str(self.term_b)+")"

class Or(Axiom):
    '''
        Class for writing Or axioms.
        Ex. A v B is written as Or(A,B)
    '''

    def __init__(self,term_a,term_b):
        super().__init__("OR")
        self.term_a=term_a
        self.term_b=term_b
        logger.debug(f"Initialised axiom Or({self.term_a},{self.term_b})")

    def __eq__(self,other):
        params=(self.type,self.term_a,self.term_b)
        params_inv=(self.type,self.term_b,self.term_a)
        return (params == other) or (params_inv == other)

    def __hash__(self):
        return hash(self.type+str(hash(self.term_a))+str(hash(self.term_b)))

    def __str__(self):
        return "("+str(self.term_a)+" OR "+str(self.term_b)+")"

class Not(Axiom):
    '''
        Class for defining Not axioms.
        Ex. ~A is written as Not(A)
    '''

    def __init__(self,term):
        super().__init__("NOT")
        self.term=term
        logger.debug(f"Initialised axiom Not({self.term})")

    def __eq__(self,other):
        return (self.type,self.term)==other

    def __hash__(self):
        return hash(self.type+str(hash(self.term)))

    def __str__(self):
        return "NOT "+str(self.term)

class ClassAssertion(Axiom):
    '''
        Defines Class assertions/ ABox assertions.
    '''

    def __init__(self,definitions,instance):
        super().__init__("ASSERT")
        self.definitions=definitions
        self.instance=instance
        logger.debug(f"Initialised axiom ASSERT {self.instance} is a {self.definitions}")

    def __eq__(self,other):
        return (self.type,self.definitions,self.instance)==other

    def __hash__(self):
        return hash(self.type+str(hash(self.definitions))+str(hash(self.instance)))

    def __str__(self):
        return "ASSERT "+str(self.instance)+" IS A "+str(self.definitions)
