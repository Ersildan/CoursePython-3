from itertools import groupby

key_func = lambda x: x > 5
numbers = [7, 6, 1, 1, 5, 10, 11, 2, 3, 4]

groups = groupby(numbers, key=key_func)

for _, group in groups:
    print(*group)