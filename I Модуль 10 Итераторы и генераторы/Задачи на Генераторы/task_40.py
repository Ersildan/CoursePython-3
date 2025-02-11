def with_previous(iterable):
    n = None
    for i in iterable:
        yield (i, n)
        n = i


numbers = [1, 2, 3, 4, 5]

print(*with_previous(numbers))