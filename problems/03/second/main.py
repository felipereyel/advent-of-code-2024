import sys
import re


def main():
    file = sys.argv[1]
    with open(file) as f:
        total = 0
        content = f.read()
        for segment in content.split("do()"):
            enabled, *_ = segment.split("don't()")
            for tuple in re.findall("mul\((\d{1,3},\d{1,3})\)", enabled):
                left, right = tuple.split(",")
                total += int(left) * int(right)

        print(total)


if __name__ == "__main__":
    main()
