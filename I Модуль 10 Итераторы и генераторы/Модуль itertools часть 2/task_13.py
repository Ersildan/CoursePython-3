from itertools import islice

def take(iterable, n):
    return islice(iterable, n)

print(*take(range(10), 5))

