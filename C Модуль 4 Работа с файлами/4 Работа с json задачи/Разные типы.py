import json

with open('data.json') as file, open('updated_data.json', 'w', encoding='utf-8') as f:

    lst = []
    data = json.load(file)

    for value in data:
        match value:
            case str(): value += '!'
            case bool(): value = (True, False)[value]
            case int(): value += 1
            case list(): value *= 2
            case dict(): value['newkey'] = None
            case None: continue
        lst.append(value)
    json.dump(lst, f, indent=3)
