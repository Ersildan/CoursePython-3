import json

with open('food_services.json', encoding='utf-8') as file:
    data = json.load(file)
    res = dict()
    for d in data:
        res[d["TypeObject"]] = res.get(d["TypeObject"], []) + [(d['Name'], d["SeatsCount"])]

    lst = []
    for k, v in res.items():
        mx = max(v, key=lambda x: x[1])
        lst.append((k, mx[0], mx[1]))
    lst = sorted(lst, key=lambda x: x[0])
    for el in lst:
        print(f"{el[0]}: {el[1]}, {el[2]}")
