from src.formula import *

def big_and(formulas: list[Formula]) -> Formula | None:
    if not formulas:
        return None

    result = formulas[0]
    for formula in formulas[1:]:
        result = And(result, formula)
    return result

def big_or(formulas: list[Formula]) -> Formula | None:
    if not formulas:
        return None

    result = formulas[0]
    for formula in formulas[1:]:
        result = Or(result, formula)
    return result

class ExerciseSubItems:
    @staticmethod
    def item_a() -> None:
        formulas = [Atom(f"p_{i}") for i in range(1, 21)]
        print(big_and(formulas))

    @staticmethod
    def item_b(n: int) -> None:
        if n <= 1:
            n = 1

        formulas = [Atom(f"p_{i}") for i in range(1, n + 1)]
        print(big_and(formulas))

    @staticmethod
    def item_c(n: int, m: int) -> None:
        if n <= 1 or m <= 1:
            n = m = 1

        formulas = []
        for i in range(1, n + 1):
            subformulas = []
            for j in range(1, m + 1):
                subformulas.append(Not(Atom(f"p_{i}_{j}")))
            formulas.append(big_and(subformulas))
        print(big_or(formulas))

    @staticmethod
    def item_d(n: int) -> None:
        if n <= 1:
            n = 1

        formulas = []
        for i in range(1, n + 1):
            formulas.append(
                And(
                    Implies(
                        Atom(f"a_{i}"),
                        Or(
                            Atom(f"a_{i + 1}"),
                            Atom(f"b_{i + 1}")
                        )
                    ),
                    Implies(
                        Atom(f"b_{i}"),
                        Or(
                            Atom(f"a_{i + 1}"),
                            Atom(f"b_{i + 1}")
                        )
                    )
                )
            )

        print(big_and(formulas))

    @staticmethod
    def item_e(n: int) -> None:
        if n <= 1:
            n = 1

        formulas = []
        for i in range(1, n + 1):
            formulas.append(Or(Atom(f"p_{i}"), Atom(f"q_{i}")))
        print(Implies(big_and(formulas), Atom(f"p_{n + 1}")))

    @staticmethod
    def item_f(n: int) -> None:
        if n <= 1:
            n = 1

        formulas = []
        for i in range(1, n + 2):
            subformulas = []
            for j in range(1, n + 1):
                subformulas.append(Atom(f"p_{i}_{j}"))
            formulas.append(big_or(subformulas))
        print(big_and(formulas))

    @staticmethod
    def item_g(n: int):
        if n <= 1:
            n = 1

        formulas = []
        for i in range(1, n + 1):
            subformulas = []
            for j in range(i + 1, n + 2):
                subsubformulas = []
                for k in range(1, n + 1):
                    subsubformulas.append(And(Atom(f"p_{i}_{j}"), Atom(f"p_{k}_{j}")))
                subformulas.append(big_or(subsubformulas))
            formulas.append(big_or(subformulas))
        print(big_or(formulas))

def main() -> None:
    pass

if __name__ == "__main__":
    main()
