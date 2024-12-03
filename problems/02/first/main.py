import sys


def dist(a, b):
    return (a - b) if a > b else (b - a)


def main():
    file = sys.argv[1]
    with open(file) as f:
        safe = []
        for line in f.readlines():
            curr_dir = 0
            report = [int(r) for r in line.split()]

            for i in range(len(report) - 1):
                dir = report[i] - report[i + 1]

                if abs(dir) not in [1, 2, 3]:
                    break

                if curr_dir == 0:
                    curr_dir = dir
                    continue

                changes = curr_dir * dir
                if changes < 0:
                    break
            else:
                safe.append(report)

        print(len(safe))


if __name__ == "__main__":
    main()
