import json
import csv

with open('students.json', encoding='utf-8') as file:
    data = json.load(file)
    lst = []
    for d in data:
        if d['age'] > 17 and d['progress'] > 74:
            lst.append([d['name'], d['phone']])

    lst = sorted(lst, key=lambda x: x[0])
    columns = ['name', 'phone']
    with open('data.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(columns)
        writer.writerows(lst)

