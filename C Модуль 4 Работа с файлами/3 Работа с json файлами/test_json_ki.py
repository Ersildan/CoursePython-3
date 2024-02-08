import json

data = {'first_name': 'Андрей', 'last_name': 'Свист'}
s = json.dumps(data)
print(s)
print()
s = json.dumps(data, ensure_ascii=False)
print(s)