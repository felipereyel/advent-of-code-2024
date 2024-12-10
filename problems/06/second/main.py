import sys
from typing import List, Tuple


# THIS TOOK 10MIN TO RUN ON THE REAL INPUT
def main():
    file = sys.argv[1]
    with open(file) as f:
        obstacles, curr_i, curr_j, max_i, max_j = read_map(f)

        visited_positions = walk_map(obstacles, curr_i, curr_j, max_i, max_j)
        if not visited_positions:
            raise Exception("already has a cycle")

        loop_obstacles = []
        for possible_obstacle in visited_positions:
            if possible_obstacle[0] == curr_i and possible_obstacle[1] == curr_j:
                continue

            new_obstacles = [*obstacles, possible_obstacle]
            new_positions = walk_map(new_obstacles, curr_i, curr_j, max_i, max_j)
            if not new_positions:
                loop_obstacles.append(possible_obstacle)

        print(len(loop_obstacles))


def walk_map(obstacles, curr_i, curr_j, max_i, max_j):
    dir_i = -1
    dir_j = 0

    visited_positions: List[Tuple[int, int, int, int]] = []
    visited_positions.append((curr_i, curr_j, dir_i, dir_j))

    while True:
        next_i = curr_i + dir_i
        next_j = curr_j + dir_j

        if next_i > max_i or next_j > max_j or next_i < 0 or next_j < 0:
            # Leave the area
            break

        if (next_i, next_j) in obstacles:
            # Turn
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
            continue

        if (next_i, next_j, dir_i, dir_j) in visited_positions:
            # Cycle
            return None

        visited_positions.append((next_i, next_j, dir_i, dir_j))
        # print(next_i, next_j, dir_i, dir_j)
        curr_i = next_i
        curr_j = next_j

    return set([(i, j) for i, j, _, _ in visited_positions])


def read_map(f):
    obstacles: List[Tuple[int, int]] = []

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

    return obstacles, curr_i, curr_j, max_i, max_j


if __name__ == "__main__":
    main()
