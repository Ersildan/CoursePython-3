from itertools import groupby

key_func = lambda x: x % 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

groups = groupby(sorted(numbers, key=key_func), key=key_func)

for _, group in groups:
    print(*group)