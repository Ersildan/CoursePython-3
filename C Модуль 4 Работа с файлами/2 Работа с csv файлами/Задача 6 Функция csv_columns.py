import csv


def csv_columns(filename):
    with open(filename, encoding='utf-8') as file:
        data = csv.DictReader(file)
        res = dict()
        for d in data:
            for k, v in d.items():
                res[k] = res.get(k, []) + [v]
        return res
