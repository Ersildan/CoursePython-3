from zipfile import ZipFile
import json


def is_correct_json(string):
    try:
        j = json.load(string)
        return j
    except:
        pass


with ZipFile("data.zip") as zp:
    lst = []
    for el in zp.infolist():
        if not el.is_dir():
            with zp.open(el, 'r') as z:
                lst.append(is_correct_json(z))
    lst = list(filter(lambda x: x is not None, lst))
    lst = list(filter(lambda x: x['team'] == 'Arsenal', lst))
    lst = sorted(lst, key=lambda x: (x['first_name'], x['last_name']))
    print(*[f"{d["first_name"]} {d['last_name']}" for d in lst], sep='\n')
