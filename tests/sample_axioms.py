import sys 

sys.path.append("/home/adityas/Projects/ALC-reasoner/")

from reasoner.knowledgebase.axioms import And,Or,Not,ClassAssertion,ABoxAxiom
from reasoner.common.constructors import Concept,All,Some,Instance

simple_or=Or(Concept("Man"),Concept("Machine"))
complex_or=Or(Or(Concept("Man"),Concept("Machine")),Concept("Robot"))
kinda_complicated_axiom=And(Or(And(Concept("Man"),Not(Concept("Machine"))),And(Concept("Machine"),Not(Concept("Man")))),Concept("Physical"))
kinda_complicated_abox=ABoxAxiom(ClassAssertion(kinda_complicated_axiom,Instance("Aditya")))


kinda_complicated_unsat_axiom=And(Or(And(Concept("Man"),Not(Concept("Machine"))),And(Concept("Machine"),Not(Concept("Man")))),And(Concept("Man"),Concept("Machine")))

kinda_complicated_unsat_abox=ABoxAxiom(ClassAssertion(kinda_complicated_unsat_axiom,Instance("Aditya")))
