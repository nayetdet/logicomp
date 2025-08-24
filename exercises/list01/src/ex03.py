from src.functions import *

def main() -> None:
    formula = Or(Not(And(Atom('p'), Atom('choveu_ontem'))), Atom('p'))
    print([str(x) for x in atoms(formula)]) # ['p', 'choveu_ontem']

if __name__ == "__main__":
    main()
