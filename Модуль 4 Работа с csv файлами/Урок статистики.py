import sys

data = [int(i) for i in sys.stdin]

if len(data) == 0:
    print('нет учеников')
else:
    mn = min(data)
    mx = max(data)
    ar = sum(data)/len(data)
    print(f'Рост самого низкого ученика: {mn}')
    print(f'Рост самого высокого ученика: {mx}')
    print(f'Средний рост: {ar}')
