from itertools import islice

print(*islice(range(10), None))
print(*islice(range(100), 5))
print(*islice(range(100), 5, 10))
print(*islice(range(100), 0, 100, 10))

'''
islice(iterable, stop)
islice(iterable, start, stop)
islice(iterable, start, stop, step)
'''
