from src.functions import *

def main() -> None:
    formula = Or(And(Atom("p"), Not(Implies(Atom("p"), Not(Atom("q"))))), Not(Atom("q")))
    print(number_of_atoms(formula)) # number of atoms((p ∧ ¬(p → ¬q)) ∨ ¬q) = 4

if __name__ == "__main__":
    main()
