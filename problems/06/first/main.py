import sys
from typing import List, Tuple


def main():
    file = sys.argv[1]
    with open(file) as f:
        obstacles: List[Tuple[int, int]] = []
        visited_positions = set()

        dir_i = -1
        dir_j = 0

        curr_i = 0
        curr_j = 0

        max_i = 0
        max_j = 0

        for i, raw_line in enumerate(f.readlines()):
            max_i = i
            for j, cell in enumerate(raw_line.strip()):
                max_j = j
                if cell == "#":
                    obstacles.append((i, j))
                elif cell == "^":
                    curr_i = i
                    curr_j = j

        visited_positions.add((curr_i, curr_j))
        while curr_i <= max_i and curr_j <= max_j:
            next_i = curr_i + dir_i
            next_j = curr_j + dir_j

            if (next_i, next_j) not in obstacles:
                visited_positions.add((curr_i, curr_j))
                curr_i = next_i
                curr_j = next_j
                continue

            if dir_i == -1 and dir_j == 0:
                dir_i = 0
                dir_j = 1
            elif dir_i == 0 and dir_j == 1:
                dir_i = 1
                dir_j = 0
            elif dir_i == 1 and dir_j == 0:
                dir_i = 0
                dir_j = -1
            elif dir_i == 0 and dir_j == -1:
                dir_i = -1
                dir_j = 0

        print(len(visited_positions))


if __name__ == "__main__":
    main()
