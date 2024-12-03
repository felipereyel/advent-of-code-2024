import sys


def dist(a, b):
    return (a - b) if a > b else (b - a)


def main():
    file = sys.argv[1]
    with open(file) as f:
        safe = []
        for line in f.readlines():
            report = [int(r) for r in line.split()]
            if is_safe(report):
                safe.append(report)
                continue

            for i in range(len(report)):
                if is_safe(report[:i] + report[i + 1 :]):
                    safe.append(report)
                    break

        print(safe, len(safe))


def is_safe(report) -> bool:
    curr_dir = 0

    for i in range(len(report) - 1):
        dir = report[i] - report[i + 1]

        if abs(dir) not in [1, 2, 3]:
            return False

        if curr_dir == 0:
            curr_dir = dir
            continue

        changes = curr_dir * dir
        if changes < 0:
            return False

    return True


if __name__ == "__main__":
    main()
