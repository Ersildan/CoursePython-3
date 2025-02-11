def with_previous(iterable):
    for el in iterable:
        yield (el, n:= None)
        n = el


numbers = [1, 2, 3, 4, 5]

print(*with_previous(numbers))