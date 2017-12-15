import logging

logger=logging.getLogger(__name__)

class Axiom(object):
    '''
        Base class in case some common methods have to be written. Should not
        be called explicitly.
    '''

    def __init__(self,_type):
        self.type=_type

    def __eq__(self,other):
        return hash(self)==hash(other)

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

    def __hash__(self):
        return hash(self.type+str(hash(self.term_a))+str(hash(self.term_b)))

    def __str__(self):
        return "("+str(self.term_a)+" AND "+str(self.term_b)+")"

    def __repr__(self):
        return str(self)

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

    def __hash__(self):
        return hash(self.type+str(hash(self.term_a))+str(hash(self.term_b)))

    def __str__(self):
        return "("+str(self.term_a)+" OR "+str(self.term_b)+")"

    def __repr__(self):
        return str(self)

class Not(Axiom):
    '''
        Class for defining Not axioms.
        Ex. ~A is written as Not(A)
    '''

    def __init__(self,term):
        super().__init__("NOT")
        self.term=term
        logger.debug(f"Initialised axiom Not({self.term})")

    def __hash__(self):
        return hash(self.type+str(hash(self.term)))

    def __repr__(self):
        return "NOT "+str(self.term)

class Subsumption(Axiom):
    '''
        Class for defining subsumptions.
    '''

    def __init__(self,axiom1,axiom2):
        super().__init__("SUBSUMPTION")
        self.axiom1=axiom1
        self.axiom2=axiom2

    def __hash__(self):
        return hash(self.type+str(hash(self.axiom1))+str(hash(self.axiom2)))

    def __repr__(self):
        return f"ALL {self.axiom1} ARE {self.axiom2}"

class ClassAssertion(Axiom):
    '''
        Defines Class assertions/ ABox assertions.
    '''

    def __init__(self,definitions,instance):
        super().__init__("C_ASSERT")
        self.definitions=definitions
        self.instance=instance
        logger.debug(f"Initialised axiom ASSERT {self.instance} is a {self.definitions}")

    def __hash__(self):
        return hash(self.type+str(hash(self.definitions))+str(hash(self.instance)))

    def __str__(self):
        return "ASSERT "+str(self.instance)+" IS A "+str(self.definitions)

class RoleAssertion(Axiom):
    '''
        Defines Role assertions/ ABox assertions.
    '''

    def __init__(self,role,instance1,instance2):
        super().__init__("R_ASSERT")
        self.role=role
        self.instance1=instance1
        self.instance2=instance2
        logger.debug(f"Initialised axiom ASSERT {self.instance1} {self.role} {self.instance2}")

    def __hash__(self):
        return hash(self.type+str(hash(self.role))+str(hash(self.instance1))+str(hash(self.instance2)))

    def __str__(self):
        return f"ASSERT {self.instance1} {self.role} {self.instance2}"

class ABoxAxiom(Axiom):
    '''
        Provides a wrapper around assertion axioms.
    '''
    
    def __init__(self,axiom):
        super().__init__("ABOX")
        self.axiom=axiom

    def __eq__(self,other):
        return self.axiom==other

    def __hash__(self):
        return hash(self.type+str(hash(self.axiom)))

    def __str__(self):
        return str(self.axiom)

    def __repr__(self):
        return str(self.axiom)

class TBoxAxiom(Axiom):
    '''
        A Wrapper for TBox axioms.
    '''

    def __init__(self,axiom):
        super().__init__("TBOX")
        self.axiom=axiom

    def __eq__(self,other):
        return self.axiom==other

    def __hash__(self):
        return hash(self.type+str(hash(self.axiom)))

    def __str__(self):
        return str(self.axiom)

    def __repr__(self):
        return str(self.axiom)
