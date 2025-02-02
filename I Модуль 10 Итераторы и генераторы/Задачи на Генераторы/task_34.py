from csv import DictReader

def func(company):
    if company['round'] == 'a': return int(company['raisedAmt'])
    else: return 0

with open('data.csv', encoding='UTF-8') as file:
    data = DictReader(file)
    print(sum(func(el) for el in data))
