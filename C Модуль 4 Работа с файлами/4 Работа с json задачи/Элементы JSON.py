import sys
import json

data = json.load(sys.stdin)

for k, v in data.items():
    if type(v) == list:
        print(f'{k}: {", ".join(list(map(str, v)))}')
    else:
        print(f'{k}: {v}')
