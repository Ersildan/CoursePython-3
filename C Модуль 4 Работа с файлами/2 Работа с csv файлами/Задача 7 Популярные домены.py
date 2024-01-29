import csv

with open('data.csv', encoding='utf-8') as file:
    data = list(csv.DictReader(file, delimiter=',', quotechar='"'))
    res = {}

    for d in data:
        k = d['email'].split('@')[1]
        res[k] = res.get(k, 0) + 1

    lst = sorted(res.items(), key=lambda x: (x[1], x[0]))

    with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONE)
        writer.writerow(['domain', 'count'])
        writer.writerows(lst)
