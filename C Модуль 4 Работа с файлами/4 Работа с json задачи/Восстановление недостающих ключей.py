import json

with (open('people.json', encoding='utf-8') as file,
      open('updated_people.json', 'w', encoding='utf-8') as f):

    data = json.load(file)

    new_dict = dict()
    for d in data:
        new_dict |= d

    new_dict = {k: None for k, v in new_dict.items()}
    lst = [new_dict | d for d in data]
    json.dump(lst, f, indent=3)
