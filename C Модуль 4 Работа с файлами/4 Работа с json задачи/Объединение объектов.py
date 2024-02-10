import json

with open('data1.json', encoding='utf-8') as file1, open('data2.json', encoding='utf-8') as file2:
    with open('data_merge.json', 'w', encoding='utf-8') as f:
        f1, f2 = json.load(file1), json.load(file2)
        res = {k: f2[k] if k in f2 else f1[k] for k, v in f1.items()}
        for k, v in f2.items():
            res[k] = res.get(k, v)
        json.dump(res, f, indent=3)
