import csv

with open('prices.csv', encoding='utf-8') as file:
    data = list(csv.DictReader(file, delimiter=';'))
    res = dict()
    for d in data:
        key = d['Магазин']
        for k, v in d.items():
            if k != 'Магазин':
                res[key] = res.get(key, []) + [(k, int(v))]

    lst = [(k, min(v, key=lambda x: x[1])) for k, v in res.items()]
    lst_ = sorted(lst, key=lambda x: (x[1][1], x[1][0]))
    print(f"{lst_[0][1][0]}: {lst_[0][0]}")
