import sys
from typing import List, Dict


def sort(p: List[str], rules: Dict[str, List[str]]) -> List[str]:
    page_size = len(p)
    for i in range(page_size - 1):
        for j in range(i + 1, page_size):
            lval = p[i]
            rval = p[j]
            rrules = rules.get(rval, [])
            if lval in rrules:
                p[i] = rval
                p[j] = lval

    return p


def main():
    file = sys.argv[1]
    with open(file) as f:
        rules: Dict[str, List[str]] = {}
        pages: List[List[str]] = []
        reading_rules = True
        for raw_line in f.readlines():
            line = raw_line.strip()
            if line == "":
                if reading_rules:
                    reading_rules = False
                    continue
                else:
                    break

            if reading_rules:
                lval, rval = line.split("|")
                lrules = rules.get(lval, [])
                rules[lval] = [*lrules, rval]

            else:
                pages.append(line.split(","))

        sorteds = []
        for page in pages:
            sorted_page = sort(page.copy(), rules)
            if sorted_page == page:
                sorteds.append(page)

        print(sum([int(s[len(s) // 2]) for s in sorteds]))


if __name__ == "__main__":
    main()
