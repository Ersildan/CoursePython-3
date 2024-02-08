import json

json_data = '''
{
   "name": "Russia",
   "phone_code": 7,
   "latitude": 60.0,
   "capital": "Moscow",
   "timezones": ["Anadyr", "Barnaul", "Moscow", "Kirov"],
   "translations": {
      "nl": "Rusland",
      "hr": "Rusija",
      "de": "Russland",
      "es": "Rusia",
      "fr": "Russie",
      "it": "Russia"
   }
}'''

data = json.loads(json_data)

print(type(data['name']) , 'name')
print(type(data['phone_code']), 'phone_code')
print(type(data['latitude']), 'latitude')
print(type(data['timezones']), 'timezones')
print(type(data['translations']), 'translations')
