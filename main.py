import sys

info = sys.argv[1]

with open(info, encoding="utf-8") as f:
    for line in f:
        print(line.strip())