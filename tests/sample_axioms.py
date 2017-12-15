import sys 

sys.path.append("/home/adityas/Projects/ALC-reasoner/")

from reasoner.knowledgebase.axioms import And,Or,Not,ClassAssertion,ABoxAxiom,RoleAssertion,TBoxAxiom,Subsumption
from reasoner.common.constructors import Concept,All,Some,Instance

simple_or=Or(Concept("Man"),Concept("Machine"))
complex_or=Or(Or(Concept("Man"),Concept("Machine")),Concept("Robot"))
kinda_complicated_axiom=And(Or(And(Concept("Man"),Not(Concept("Machine"))),And(Concept("Machine"),Not(Concept("Man")))),Concept("Physical"))
kinda_complicated_abox=ABoxAxiom(ClassAssertion(kinda_complicated_axiom,Instance("Aditya")))


kinda_complicated_unsat_axiom=And(Or(And(Concept("Man"),Not(Concept("Machine"))),And(Concept("Machine"),Not(Concept("Man")))),And(Concept("Man"),Concept("Machine")))

kinda_complicated_unsat_abox=ABoxAxiom(ClassAssertion(kinda_complicated_unsat_axiom,Instance("Aditya")))

simple_and_abox=ABoxAxiom(ClassAssertion(And(Concept("Man"),Concept("Machine")),Instance("Aditya")))

simple_or_abox=ABoxAxiom(ClassAssertion(simple_or,Instance("Aditya")))

consistent_complex_abox=[
ABoxAxiom(ClassAssertion(Or(And(Concept("Man"),Not(Concept("Machine"))),And(Concept("Machine"),Not(Concept("Man")))),Instance("Aditya"))),
ABoxAxiom(ClassAssertion(And(Concept("Man"),Concept("Machine")),Instance("Arnold")))]

inconsistent_complex_abox=[
ABoxAxiom(ClassAssertion(Or(And(Concept("Man"),Not(Concept("Machine"))),And(Concept("Machine"),Not(Concept("Man")))),Instance("Aditya"))),
ABoxAxiom(ClassAssertion(And(Concept("Man"),Not(Concept("Man"))),Instance("Arnold")))]

consistent_abox=[
ABoxAxiom(ClassAssertion(Concept("Man"),Instance("Aditya"))),
ABoxAxiom(ClassAssertion(And(Concept("Machine"),Not(Concept("Man"))),Instance("HAL"))),
ABoxAxiom(ClassAssertion(Some("hasComputer",Concept("Laptop")),Instance("Aditya"))),
ABoxAxiom(ClassAssertion(All("hasComputer",Not(Concept("Man"))),Instance("Aditya"))),
TBoxAxiom(Subsumption(Concept("Man"),Concept("Biological")))
]


