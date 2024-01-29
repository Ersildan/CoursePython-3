import csv

with open('deniro.csv', encoding='utf-8') as file:
    num = int(input()) - 1
    rows = csv.reader(file)
    for row in sorted(rows, key=lambda x: int(x[num]) if x[num].isdigit() == True else x[num]):
        print(",".join(row))
