import sys


def main():
    file = sys.argv[1]
    with open(file) as f:
        lefts = []
        rights = {}

        for line in f.readlines():
            [left_raw, right_raw] = line.split()
            lefts.append(int(left_raw.strip()))

            right = int(right_raw.strip())
            if rights.get(right):
                rights[right] += 1
            else:
                rights[right] = 1

        similarity = 0
        for left in lefts:
            similarity += rights.get(left, 0) * left

        print(similarity)


if __name__ == "__main__":
    main()
