import csv


def condense_csv(filename, id_name):
    with open(filename, encoding='utf-8') as file:
        data = list(csv.reader(file))
        res = dict()
        for i in data:
            res[id_name] = res.get(id_name, []) + [i[0]]
            res[i[1]] = res.get(i[1], []) + [i[2]]

        res[id_name] = sorted(set(res.get(id_name)))
        matrix = [_ for _ in res.values()]
        row = [_ for _ in zip(*matrix)]

        with open('condensed.csv', 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONE)
            writer.writerow([_ for _ in res.keys()])
            writer.writerows(row)


print(condense_csv('data2.csv', id_name="ID"))
