import json

with (open('countries.json', encoding='utf-8') as file,
      open('religion.json', 'w', encoding='utf-8') as f):
    data = json.load(file)

    res = dict()
    for d in data:
        k, v = d["religion"], d['country']
        res[k] = res.get(k, []) + [v]
    json.dump(res, f, indent=3)
