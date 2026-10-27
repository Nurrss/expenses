import sys, csv

info = sys.argv[1]

category_list = {}
date_list = {}

def calc(date, category , amount):
    date_list[date] = date_list.get(date,0) + amount
    category_list[category] = category_list.get(category,0) + amount

def write(c_list, d_list):
    text = "По категориям: \n\n"
    for key , value in c_list.items():
        text += f"{key}: {value}\n"
    text += "\n\n"
    text += "По месяцам: \n\n"
    for key , value in d_list.items():
        text += f"{key}: {value}\n"
    return text
    

with open(info, encoding="utf-8") as f:
    for row in csv.DictReader(f):
        calc(row["date"][:7], row["category"], float(row["amount"]))
print(write(category_list, date_list))


