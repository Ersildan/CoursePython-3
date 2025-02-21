from itertools import islice

def take_nth(iterable, n):
    return next(islice(iterable, n-1, n), None)

numbers = [11, 22, 33, 44, 55]

print(take_nth(numbers, 3))
