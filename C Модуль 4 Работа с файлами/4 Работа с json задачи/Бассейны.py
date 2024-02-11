import json
from datetime import datetime as dt


def foo(time_work):
    pn = "%H:%M"
    t1, t2 = time_work.split('-')
    open_pool, close_pool = dt(1900, 1, 1, 10).time(), dt(1900, 1, 1, 12).time()
    t1, t2 = dt.strptime(t1, pn).time(), dt.strptime(t2, pn).time()
    return True if t1 == open_pool and t2 >= close_pool else False


with open("pools.json", encoding='utf-8') as file:
    data = json.load(file)
    lst = []
    for d in data:
        if foo(d["WorkingHoursSummer"]["Понедельник"]):
            lst.append((d["DimensionsSummer"]["Length"], d["DimensionsSummer"]["Width"], d["Address"]))
    lst = sorted(lst, key=lambda x: (x[0], x[1]))[::-1]
    print(f"{lst[0][0]}x{lst[0][1]}", lst[0][2], sep='\n')
