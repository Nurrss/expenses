with open("expenses.csv", encoding="utf-8") as f:
    for line in f:
        print(line.strip())