import sys

data = [int(i) for i in sys.stdin]
lst, lst_ = [], []

for i in range(1, len(data)-1):
    lst.append(2*data[i] == data[i-1] + data[i+1])
    lst_.append(data[i]**2 == data[i-1] * data[i+1])

if all(lst):
    print('Арифметическая прогрессия')
elif all(lst_):
    print('Геометрическая прогрессия')
else:
    print('Не прогрессия')
