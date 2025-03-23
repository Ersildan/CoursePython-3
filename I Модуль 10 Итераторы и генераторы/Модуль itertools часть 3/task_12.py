from itertools import tee, chain

def ncycles(iterable, times):
    return chain(*tee(iterable, times))

print(*ncycles([1, 2, 3, 4], 3))