from src.formula import *

def substitution(formula: Formula, old_subformula: Formula, new_subformula: Formula) -> Formula:
    if formula == old_subformula:
        return new_subformula

    if isinstance(formula, Atom):
        return formula

    if isinstance(formula, Not):
        return Not(substitution(formula.inner, old_subformula, new_subformula))

    if hasattr(formula, "left") and hasattr(formula, "right"):
        left = substitution(formula.left, old_subformula, new_subformula)
        right = substitution(formula.right, old_subformula, new_subformula)
        return type(formula)(left, right) # Chamada do construtor da classe a partir da instância

    return formula

def main() -> None:
    formula = Implies(And(Atom("p"), Not(Atom("q"))), Atom("r")) # ((p ∧ ¬q) → r)
    old_subformola = Not(Atom("q")) # (¬q)
    new_subformola = Or(Atom("r"), Atom("t")) # (r ∨ t)
    print(substitution(formula, old_subformola, new_subformola)) # ((p ∧ (r ∨ t)) → r).

if __name__ == "__main__":
    main()
