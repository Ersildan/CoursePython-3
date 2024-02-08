import json

data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}

json_data = json.dumps(data, indent=3, separators=(' ;', ' = '))

print(json_data)
