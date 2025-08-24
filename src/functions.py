"""The goal in this module is to define functions that take a formula as input and
do some computation on its syntactic structure. """

from formula import *

def length(formula: Formula):
    """Determines the length of a formula in propositional logic."""
    if isinstance(formula, Atom):
        return 1
    if isinstance(formula, Not):
        return length(formula.inner) + 1
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        return length(formula.left) + length(formula.right) + 1

def subformulas(formula: Formula):
    """Returns the set of all subformulas of a formula.

    For example, observe the piece of code below.

    my_formula = Implies(Atom('p'), Or(Atom('p'), Atom('s')))
    for subformula in subformulas(my_formula):
        print(subformula)

    This piece of code prints p, s, (p v s), (p → (p v s))
    (Note that there is no repetition of p)
    """
    if isinstance(formula, Atom):
        return {formula}
    if isinstance(formula, Not):
        return {formula}.union(subformulas(formula.inner))
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        sub1 = subformulas(formula.left)
        sub2 = subformulas(formula.right)
        return {formula}.union(sub1).union(sub2)

#  we have shown in class that, for all formula A, len(subformulas(A)) <= length(A).

def atoms(formula: Formula):
    """Returns the set of all atoms occurring in a formula.

    For example, observe the piece of code below.

    my_formula = Implies(Atom('p'), Or(Atom('p'), Atom('s')))
    for atom in atoms(my_formula):
        print(atom)

    This piece of code above prints: p, s
    (Note that there is no repetition of p)
    """
    if isinstance(formula, Atom):
        return {formula}
    if isinstance(formula, Not):
        return atoms(formula.inner)
    if hasattr(formula, "left") and hasattr(formula, "right"):
        return atoms(formula.left).union(atoms(formula.right))
    return set()

def number_of_atoms(formula: Formula):
    """Returns the number of atoms occurring in a formula.
    For instance,
    number_of_atoms(Implies(Atom('q'), And(Atom('p'), Atom('q'))))

    must return 3 (Observe that this function counts the repetitions of atoms)
    """
    if isinstance(formula, Atom):
        return 1
    if isinstance(formula, Not):
        return number_of_atoms(formula.inner)
    if hasattr(formula, "left") and hasattr(formula, "right"):
        return number_of_atoms(formula.left) + number_of_atoms(formula.right)
    return 0

def number_of_connectives(formula: Formula):
    if isinstance(formula, Atom):
        return 1
    if isinstance(formula, Not):
        return number_of_connectives(formula.inner) + 1
    if hasattr(formula, "left") and hasattr(formula, "right"):
        return number_of_connectives(formula.left) + number_of_connectives(formula.right) + 1
    return None

def is_literal(formula: Formula):
    return isinstance(formula, Atom) or (isinstance(formula, Not) and isinstance(formula.inner, Atom))

def substitution(formula: Formula, old_subformula: Formula, new_subformula: Formula):
    """Returns a new formula obtained by replacing all occurrences
    of old_subformula in the input formula by new_subformula."""
    if formula == old_subformula:
        return new_subformula

    if isinstance(formula, Atom):
        return formula

    if isinstance(formula, Not):
        return Not(substitution(formula.inner, old_subformula, new_subformula))

    if hasattr(formula, "left") and hasattr(formula, "right"):
        left = substitution(formula.left, old_subformula, new_subformula)
        right = substitution(formula.right, old_subformula, new_subformula)
        return type(formula)(left, right)

    return formula

def is_clause(formula: Formula):
    if is_literal(formula):
        return True
    if isinstance(formula, Or):
        return is_clause(formula.left) and is_clause(formula.right)
    return False

def is_negation_normal_form(formula: Formula):
    """Returns True if formula is in negation normal form.
    Returns False, otherwise."""
    if isinstance(formula, Atom):
        return True
    if isinstance(formula, Not):
        return isinstance(formula.inner, Atom) # A parte de dentro do not não pode ser uma fórmula
    if hasattr(formula, "left") and hasattr(formula, "right"):
        return is_negation_normal_form(formula.left) and is_negation_normal_form(formula.right)
    return False

def is_cnf(formula: Formula):
    if is_clause(formula):
        return True
    if isinstance(formula, And):
        return is_cnf(formula.left) and is_cnf(formula.right)
    return False

def is_term(formula: Formula):
    """Returns True if formula is a term. It returns False, otherwise"""
    if is_literal(formula):
        return True
    if isinstance(formula, And):
        return is_term(formula.left) and is_term(formula.right)
    return False

def is_dnf(formula: Formula):
    """Returns True if formula is in disjunctive normal form.
    Returns False, otherwise."""
    if is_term(formula):
        return True
    if isinstance(formula, Or):
        return is_dnf(formula.left) and is_dnf(formula.right)
    return False

def is_decomposable_negation_normal_form(formula: Formula):
    """Returns True if formula is in decomposable negation normal form.
    Returns False, otherwise."""
    if not is_negation_normal_form(formula):
        return False

    for subformula in subformulas(formula):
        if isinstance(subformula, And):
            left_atoms, right_atoms = atoms(subformula.left), atoms(subformula.right)
            if left_atoms.intersection(right_atoms):
                return False

    return True
