import json
import csv

with open('playgrounds.csv', encoding='utf-8') as file:
    data = list(csv.DictReader(file, delimiter=';'))
    res = dict()
    for d in data:
        res.setdefault(d["AdmArea"], {}).setdefault(d['District'], []).append(d['Address'])
    with open('addresses.json', 'w', encoding='utf-8') as f:
        json.dump(res, f, indent=3, ensure_ascii=False)
