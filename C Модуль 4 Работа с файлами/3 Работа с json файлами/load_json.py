import json

with open('data.json') as file:
    data = json.load(file)
    for k, v in data.items():
        if type(v) == list:
            print(f"{k}: {", ".join(v)}")
        else:
            print(f"{k}: {v}")
