import csv

with open('wifi.csv', encoding='utf-8') as file:
    data = list(csv.DictReader(file, delimiter=';', quotechar='"'))
    res = {}

    for d in data:
        k = d['district']
        v = d['number_of_access_points']
        if 'город Москва' in d['location']:
            res[k] = res.get(k, 0) + int(v)

    for i in sorted(res.items(), key=lambda x: (x[1], x[0]))[::-1]:
        print(f"{i[0]}: {i[1]}")
