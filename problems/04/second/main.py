import sys
from typing import List, Tuple


def check_x_mas(p: List[List[str]], x: int, y: int) -> List[Tuple]:
    rows = len(p)
    cols = len(p[0])

    matches = []

    if x >= 1 and y >= 1 and x <= (rows - 1 - 1) and y <= (cols - 1 - 1):
        A = p[x - 1][y - 1] + p[x][y] + p[x + 1][y + 1]
        B = p[x - 1][y + 1] + p[x][y] + p[x + 1][y - 1]

        if (A == "MAS" or A == "SAM") and (B == "MAS" or B == "SAM"):
            matches.append((x, y, A, B))

    return matches


def main():
    file = sys.argv[1]
    with open(file) as f:
        As = []
        puzzle = []
        for x, line in enumerate(f.readlines()):
            line_list = list(line.strip())
            puzzle.append(line_list)
            for y, char in enumerate(line_list):
                if char == "A":
                    As.append((x, y))

        matches = []
        for x, y in As:
            try:
                for match in check_x_mas(puzzle, x, y):
                    matches.append(match)
            except Exception as e:
                print(x, y)
                raise e

        print(len(matches))


if __name__ == "__main__":
    main()
