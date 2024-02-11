import csv
import json

with open('exam_results.csv', encoding='utf-8') as file:
    file.seek(38)
    columns = ['name', 'surname', 'best_score', 'date_and_time', 'email']
    data = list(csv.DictReader(file, delimiter=',', fieldnames=columns))

    res = dict()
    for d in data:
        res[d['email']] = res.get(d['email'], []) + [d]

    key = sorted(res)
    lst_dicts = [max(res[k], key=lambda x: (x['best_score'], x['date_and_time'])) for k in key]

    for d in lst_dicts:
        d['best_score'] = int(d['best_score'])

    with open('best_scores.json', 'w', encoding='utf-8') as f:
        json.dump(lst_dicts, f, indent=3)
