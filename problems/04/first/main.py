import sys
from typing import List, Tuple


def check_xmas(p: List[List[str]], x: int, y: int) -> List[Tuple]:
    rows = len(p)
    cols = len(p[0])

    matches = []

    # N
    if x >= 3:
        if p[x][y] + p[x - 1][y] + p[x - 2][y] + p[x - 3][y] == "XMAS":
            matches.append((x, y, "N"))

    # NO
    if x >= 3 and y >= 3:
        if p[x][y] + p[x - 1][y - 1] + p[x - 2][y - 2] + p[x - 3][y - 3] == "XMAS":
            matches.append((x, y, "NO"))

    # NL
    if x >= 3 and y <= (cols - 4):
        if p[x][y] + p[x - 1][y + 1] + p[x - 2][y + 2] + p[x - 3][y + 3] == "XMAS":
            matches.append((x, y, "NL"))

    # O
    if y >= 3:
        if p[x][y] + p[x][y - 1] + p[x][y - 2] + p[x][y - 3] == "XMAS":
            matches.append((x, y, "O"))

    # L
    if y <= (cols - 4):
        if p[x][y] + p[x][y + 1] + p[x][y + 2] + p[x][y + 3] == "XMAS":
            matches.append((x, y, "L"))

    # S
    if x <= (rows - 4):
        if p[x][y] + p[x + 1][y] + p[x + 2][y] + p[x + 3][y] == "XMAS":
            matches.append((x, y, "S"))

    # SO
    if x <= (rows - 4) and y >= 3:
        if p[x][y] + p[x + 1][y - 1] + p[x + 2][y - 2] + p[x + 3][y - 3] == "XMAS":
            matches.append((x, y, "SO"))

    # SL
    if x <= (rows - 4) and y <= (cols - 4):
        if p[x][y] + p[x + 1][y + 1] + p[x + 2][y + 2] + p[x + 3][y + 3] == "XMAS":
            matches.append((x, y, "SL"))

    return matches


def main():
    file = sys.argv[1]
    with open(file) as f:
        xs = []
        puzzle = []
        for x, line in enumerate(f.readlines()):
            line_list = list(line.strip())
            puzzle.append(line_list)
            for y, char in enumerate(line_list):
                if char == "X":
                    xs.append((x, y))

        matches = []
        for x, y in xs:
            try:
                for match in check_xmas(puzzle, x, y):
                    matches.append(match)
            except Exception as e:
                print(x, y)
                raise e

        print(len(matches))


if __name__ == "__main__":
    main()
