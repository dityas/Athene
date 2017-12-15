# Athene - A description logic reasoner.
=========================================

## Introduction.

Athene is a description logic reasoner written completely in native python. The current version is a beta and only supports ALC. But it can easily be extended by adding
tableau rules. Athene was written with the intent of having a readable educational semantic reasoner which can be easily extended for various description logics. 

Currently supported reasoning services are:

* Consistency check. (Reports consistency of the ontology)

* Satisfiability check. (Reports if the current axiom satisfies the ontology without actually adding it.)

The core tableau reasoning procedures are written in procedural python instead of object oriented code to support optimizations and multiprocessing.

## Tests.
Athene is still not a full feldged reasoner. For instance it does not yet support role axioms in the TBox. Below are the results of a few tests on small ontologies.

### Test 1.

###### Ontology.
```python
ABoxAxiom(ClassAssertion(Concept("Man"),Instance("Aditya")))
TBoxAxiom(Subsumption(Concept("Man"),Concept("Biological")))
```

###### Results.

KB: 
```python
[ASSERT Aditya IS A Man, ALL Man ARE Biological]
```

Output:
```python
Computed models are.
[ { 'Aditya': ( {'ALL': set(), 'AND': set(), 'OR': set(), 'SOME': set()},
                {Man, Biological},
                True,
                {})}]
```

### Test 2.

###### Ontology.
```python
ABoxAxiom(ClassAssertion(Concept("Man"),Instance("Aditya")))
ABoxAxiom(ClassAssertion(Concept("Machine"),Instance("Icarus")))
TBoxAxiom(Subsumption(Concept("Man"),Concept("Biological")))
```

###### Results.

KB: 
```python
[ASSERT Icarus IS A Machine, ASSERT Aditya IS A Man, ALL Man ARE Biological]
```

Output:
```python
Computed models are.
[ { 'Aditya': ( {'ALL': set(), 'AND': set(), 'OR': set(), 'SOME': set()},
                {Man, Biological},
                True,
                {}),
    'Icarus': ( {'ALL': set(), 'AND': set(), 'OR': set(), 'SOME': set()},
                {NOT Man, Machine},
                True,
                {})},
  { 'Aditya': ( {'ALL': set(), 'AND': set(), 'OR': set(), 'SOME': set()},
                {Man, Biological},
                True,
                {}),
    'Icarus': ( {'ALL': set(), 'AND': set(), 'OR': set(), 'SOME': set()},
                {Biological, Machine},
                True,
                {})}]

```

### Test 3.

###### Ontology.
```python
ABoxAxiom(ClassAssertion(Concept("Man"),Instance("Aditya")))
ABoxAxiom(ClassAssertion(Concept("Machine"),Instance("Icarus")))
TBoxAxiom(Subsumption(Concept("Man"),Concept("Biological")))
TBoxAxiom(Subsumption(Concept("Machine"),Not(Concept("Man"))))
TBoxAxiom(Subsumption(Concept("Biological"),Concept("Man")))
```

###### Results.

KB: 
```python
[ ASSERT Icarus IS A Machine,
  ASSERT Aditya IS A Man,
  ALL Man ARE Biological,
  ALL Machine ARE NOT Man,
  ALL Biological ARE Man]
```

Output:
```python
Computed models are.
[ { 'Aditya': ( {'ALL': set(), 'AND': set(), 'OR': set(), 'SOME': set()},
                {NOT Machine, Man, Biological},
                True,
                {}),
    'Icarus': ( {'ALL': set(), 'AND': set(), 'OR': set(), 'SOME': set()},
                {NOT Biological, NOT Man, Machine},
                True,
                {})}]
```

### Test 4.

###### Ontology.
```python

ABoxAxiom(ClassAssertion(Concept("Man"),Instance("Aditya")))
ABoxAxiom(ClassAssertion(And(Concept("Machine"),Concept("Man")),Instance("Adam")))
TBoxAxiom(Subsumption(Concept("Man"),Concept("Biological")))
TBoxAxiom(Subsumption(Concept("Machine"),Not(Concept("Man"))))
TBoxAxiom(Subsumption(Concept("Biological"),Concept("Man")))
```

###### Results.

KB: 
```python
[ ASSERT Aditya IS A Man,
  ASSERT Adam IS A (Machine AND Man),
  ALL Man ARE Biological,
  ALL Machine ARE NOT Man,
  ALL Biological ARE Man]

```

Output:
```python
Computed models are.
[]
```

### Test 5.

###### Ontology.
```python
ABoxAxiom(ClassAssertion(Concept("Man"),Instance("Aditya")))
ABoxAxiom(ClassAssertion(And(Concept("Machine"),Concept("Man")),Instance("Adam")))
TBoxAxiom(Subsumption(Concept("Man"),Concept("Biological")))
TBoxAxiom(Subsumption(Concept("Biological"),Concept("Man")))
TBoxAxiom(Subsumption(And(Concept("Machine"),Concept("Man")),Concept("Augmented")))
```

###### Results.

KB: 
```python
[ ASSERT Adam IS A (Machine AND Man),
  ASSERT Aditya IS A Man,
  ALL Man ARE Biological,
  ALL (Machine AND Man) ARE Augmented,
  ALL Biological ARE Man]
```

Output:
```python
Computed models are.
[ { 'Adam': ( {'ALL': set(), 'AND': set(), 'OR': set(), 'SOME': set()},
              {Augmented, Man, Biological, Machine},
              True,
              {}),
    'Aditya': ( {'ALL': set(), 'AND': set(), 'OR': set(), 'SOME': set()},
                {NOT Machine, Man, Biological},
                True,
                {})},
  { 'Adam': ( {'ALL': set(), 'AND': set(), 'OR': set(), 'SOME': set()},
              {Augmented, Man, Biological, Machine},
              True,
              {}),
    'Aditya': ( {'ALL': set(), 'AND': set(), 'OR': set(), 'SOME': set()},
                {Augmented, Man, Biological},
                True,
                {})}]
```
