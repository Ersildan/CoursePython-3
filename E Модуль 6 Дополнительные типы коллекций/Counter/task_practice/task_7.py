import csv
from collections import Counter

with open('name_log.csv', encoding='UTF-8') as file:
    data = list(csv.DictReader(file, delimiter=','))
    print(*[f"{mail[0]}: {mail[1]}" for mail in sorted(Counter([i['email'] for i in data]).items())], sep='\n')
