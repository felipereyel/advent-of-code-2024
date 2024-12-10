import sys
from typing import List, Tuple


def concat(a: int, b: int):
    return int(f"{a}{b}")


def operand_reducer(operands: List[int]) -> List[int]:
    n_operands = len(operands)
    if n_operands == 0:
        raise Exception("empty operands")

    if n_operands == 1:
        return operands

    *others, rmost = operands

    others_value = operand_reducer(others)
    plus = [v + rmost for v in others_value]
    mult = [v * rmost for v in others_value]
    conc = [concat(v, rmost) for v in others_value]

    return [*plus, *mult, *conc]


def main():
    file = sys.argv[1]
    with open(file) as f:
        equations: List[Tuple[int, List[int]]] = []

        for _, raw_line in enumerate(f.readlines()):
            raw_value, raw_operands = raw_line.strip().split(": ")
            equations.append(
                (int(raw_value), [int(op) for op in raw_operands.strip().split(" ")])
            )

        good_values = []
        for value, operands in equations:
            all_values = operand_reducer(operands)
            if value in all_values:
                good_values.append(value)

        print(sum(good_values))


if __name__ == "__main__":
    main()
