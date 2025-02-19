from itertools import dropwhile

def drop_this(iterable, obj):
    yield from dropwhile(lambda x: x == obj, iterable)


numbers = [0, 0, 0, 1, 2, 3]

print(*drop_this(numbers, 0))
