import csv
from datetime import datetime as dt

with open('name_log.csv', encoding='utf-8') as file:
    pn = '%d/%m/%Y %H:%M'
    res, res_ = dict(), dict()
    data = list(csv.DictReader(file, delimiter=','))

    for d in data:
        k, v = d['email'], [(d['username'], dt.strptime(d['dtime'], pn))]
        res[k] = res.get(k, []) + v
    for key, val in res.items():
        res_[key] = res_.get(key, max(val, key=lambda x: x[1]))

    lst = sorted(res_.items(), key=lambda x: x[0])
    new_lst = ['username,email,dtime'] + [f"{i[1][0]},{i[0]},{dt.strftime(i[1][1], pn)}" for i in lst]
    print(*new_lst, sep='\n')
