from itertools import groupby

numbers = [1, 1, 1, 7, 7, 7, 7, 15, 7, 7, 7]

group_iter = groupby(numbers)

for key, values in group_iter:
    print(f'{key}: {list(values)}')            # преобразуем итератор в список
    