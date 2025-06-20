from re import search
import sys

for el in sys.stdin.read().splitlines():
    try:
        match = search(r'(\d{1,3})([ -])(\d{1,3})\2(\d{4,10})', el)
        print(f'Код страны: {match.group(1)}, Код города: {match.group(3)}, Номер: {match.group(4)}')
    except:
        ...
