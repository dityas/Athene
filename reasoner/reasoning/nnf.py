import logging

logger=logging.getLogger(__name__)

from ..common.constructors import Concept,Some,All
from ..knowledgebase.axioms import And,Or,Not

def NNF(axiom):
    '''
        Recursively converts axioms to NNF.
    '''
    logger.debug(f"Converting {axiom} to NNF.")

    if axiom.type=="CONCEPT" or (axiom.type=="NOT" and axiom.term.type=="CONCEPT") or axiom.type=="R_ASSERT":
        return axiom

    elif axiom.type=="NOT" and axiom.term.type=="NOT":
        return NNF(axiom.term.term)

    elif axiom.type=="NOT" and axiom.term.type=="SOME":
        return All(axiom.term.name,NNF(Not(axiom.term.concept)))

    elif axiom.type=="NOT" and axiom.term.type=="ALL":
        return Some(axiom.term.name,NNF(Not(axiom.term.concept)))

    elif axiom.type=="NOT" and axiom.term.type=="OR":
        return And(NNF(Not(axiom.term.term_a)),NNF(Not(axiom.term.term_b)))

    elif axiom.type=="NOT" and axiom.term.type=="AND":
        return Or(NNF(Not(axiom.term.term_a)),NNF(Not(axiom.term.term_b)))

    elif axiom.type=="SOME":
        return Some(axiom.name,NNF(axiom.concept))

    elif axiom.type=="ALL":
        return All(axiom.name,NNF(axiom.concept))

    elif axiom.type=="OR":
        return Or(NNF(axiom.term_a),NNF(axiom.term_b))

    elif axiom.type=="AND":
        return And(NNF(axiom.term_a),NNF(axiom.term_b))

    elif axiom.type=="SUBSUMPTION":
        return Or(NNF(Not(axiom.axiom1)),NNF(axiom.axiom2))

