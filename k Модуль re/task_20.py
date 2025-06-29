from re import finditer

result = finditer(r'(\d\d):(\d\d)', 'You can call me from 10:00 to 12:00')

for match_obj in result:
    print(match_obj.groups())