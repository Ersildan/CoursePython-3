import csv

with open('titanic.csv', encoding='utf-8') as file:
    mans, women = [], []
    data = list(csv.DictReader(file, delimiter=';', quotechar='"'))

    for d in data:
        if d['survived'] == '1' and float(d['age']) < 18 and d['sex'] == 'male':
            mans.append(d['name'])
        elif d['survived'] == '1' and float(d['age']) < 18 and d['sex'] == 'female':
            women.append(d['name'])

    print(*mans, *women, sep='\n')
