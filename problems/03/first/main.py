import sys
import re 

def main():
    file = sys.argv[1]
    with open(file) as f:
        total = 0
        content = f.read()
        for tuple in re.findall("mul\((\d{1,3},\d{1,3})\)", content):
            left, right = tuple.split(",")
            total += int(left) * int(right)
            
        print(total)
        

if __name__ == "__main__":
    main()
