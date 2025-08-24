from src.formula import *

def formula_height(formula: Formula) -> int:
    if isinstance(formula, Atom):
        return 0
    if isinstance(formula, Not):
        return formula_height(formula.inner) + 1
    if hasattr(formula, "left") and hasattr(formula, "right"):
        return max(formula_height(formula.left), formula_height(formula.right)) + 1
    return 0

def main() -> None:
    formula = Or(Implies(Atom("p"), And(Atom("q"), Atom("r"))), Not(Atom("s")))
    print(formula_height(formula)) # formula_height((p → (q ∧ r)) ∨ ¬s) = 3

if __name__ == "__main__":
    main()
