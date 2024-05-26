import json
from collections import ChainMap

with open('zoo.json', encoding="utf-8") as file:
    txt = json.load(file)
    print(sum(ChainMap(*txt).values()))
