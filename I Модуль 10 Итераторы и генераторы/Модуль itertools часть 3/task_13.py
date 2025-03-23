from itertools import zip_longest

def grouper(iterable, n):
    return zip_longest(*[iter(iterable)] * n)


iterator = iter([1, 2, 3])

print(*grouper(iterator, 5))