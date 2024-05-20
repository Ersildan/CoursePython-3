from collections import ChainMap

info = ChainMap({'name': 'Rose', 'age': 17},
                {'country': 'USA', 'city': 'Seattle'})

print(info['hobby'])