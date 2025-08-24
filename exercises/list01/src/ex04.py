from src.functions import *

def main() -> None:
    formula1 = Or(And(And(Atom("p"), Not(And(Atom("q"), Atom("r")))), Not(Atom("r"))), Atom("s")) # ((p∧(¬(q∧r)))∧(¬r))∨s
    print(is_negation_normal_form(formula1)) # False

    formula2 = Or(And(And(Atom("p"), And(Not(Atom("q")), Atom("r"))), Not(Atom("r"))), Atom("s")) # ((p∧((¬q)∧r))∧(¬r))∨s
    print(is_negation_normal_form(formula2)) # True

if __name__ == "__main__":
    main()
