import csv

with open('exam_results.csv', encoding='utf-8') as file:
    data = list(csv.DictReader(file, delimiter=','))

    for d in data:
        print(d)
