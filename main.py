import sys, csv

info = sys.argv[1]

with open(info, encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row["date"], row["category"], row["amount"])