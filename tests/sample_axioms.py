import sys 

sys.path.append("/home/adityas/Projects/ALC-reasoner/")

from reasoner.knowledgebase.axioms import And,Or,Not,ClassAssertion
from reasoner.common.constructors import Concept,All,Some,Instance

simple_or=Or(Concept("Man"),Concept("Machine"))
complex_or=Or(Or(Concept("Man"),Concept("Machine")),Concept("Robot"))
kinda_complicated_axiom=And(Or(And(Concept("Man"),Not(Concept("Machine"))),And(Concept("Machine"),Not(Concept("Man")))),Concept("Physical"))
