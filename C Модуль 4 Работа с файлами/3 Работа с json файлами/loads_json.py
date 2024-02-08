import json

json_data = '{"name": "Russia", "phone_code": 7, "capital": "Moscow", "currency": "RUB"}'

data = json.loads(json_data)
print(type(data))
print(data)
