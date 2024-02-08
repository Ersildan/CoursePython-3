import json

data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}

json_data1 = json.dumps(data, indent=3)
json_data2 = json.dumps(data, indent=3, sort_keys=True)

print(json_data1)
print(json_data2)