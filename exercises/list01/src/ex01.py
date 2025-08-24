from src.functions import *

def main() -> None:
    formula = Or(Not(And(Atom('p'), Atom('choveu_ontem'))), Atom('p'))
    print(number_of_connectives(formula)) # 6

if __name__ == "__main__":
    main()
