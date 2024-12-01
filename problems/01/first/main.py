import sys


def dist(a, b):
    return (a - b) if a > b else (b - a)


def main():
    file = sys.argv[1]
    with open(file) as f:
        lefts = []
        rights = []
        for line in f.readlines():
            [left, right] = line.split()
            lefts.append(int(left.strip()))
            rights.append(int(right.strip()))

        lefts.sort()
        rights.sort()

        total_dist = sum([dist(left, right) for left, right in zip(lefts, rights)])
        print(total_dist)


if __name__ == "__main__":
    main()
