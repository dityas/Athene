import sys 

sys.path.append("/home/adityas/Projects/ALC-reasoner/")

from reasoner.knowledgebase.axioms import And,Or,Not,ClassAssertion,ABoxAxiom,RoleAssertion,TBoxAxiom,Subsumption
from reasoner.common.constructors import Concept,All,Some,Instance



little_kb=[
ABoxAxiom(ClassAssertion(Concept("Man"),Instance("Aditya"))),
TBoxAxiom(Subsumption(Concept("Man"),Concept("Biological")))]

small_kb=[
ABoxAxiom(ClassAssertion(Concept("Man"),Instance("Aditya"))),
ABoxAxiom(ClassAssertion(Concept("Machine"),Instance("Icarus"))),
TBoxAxiom(Subsumption(Concept("Man"),Concept("Biological")))]

simple_kb=[
ABoxAxiom(ClassAssertion(Concept("Man"),Instance("Aditya"))),
ABoxAxiom(ClassAssertion(Concept("Machine"),Instance("Icarus"))),
TBoxAxiom(Subsumption(Concept("Man"),Concept("Biological"))),
TBoxAxiom(Subsumption(Concept("Machine"),Not(Concept("Man")))),
TBoxAxiom(Subsumption(Concept("Biological"),Concept("Man")))]

inconsistent_test_kb=[
ABoxAxiom(ClassAssertion(Concept("Man"),Instance("Aditya"))),
ABoxAxiom(ClassAssertion(And(Concept("Machine"),Concept("Man")),Instance("Adam"))),
TBoxAxiom(Subsumption(Concept("Man"),Concept("Biological"))),
TBoxAxiom(Subsumption(Concept("Machine"),Not(Concept("Man")))),
TBoxAxiom(Subsumption(Concept("Biological"),Concept("Man")))]

yet_another_kb=[
ABoxAxiom(ClassAssertion(Concept("Man"),Instance("Aditya"))),
ABoxAxiom(ClassAssertion(And(Concept("Machine"),Concept("Man")),Instance("Adam"))),
TBoxAxiom(Subsumption(Concept("Man"),Concept("Biological"))),
TBoxAxiom(Subsumption(Concept("Biological"),Concept("Man"))),
TBoxAxiom(Subsumption(And(Concept("Machine"),Concept("Man")),Concept("Augmented")))]


