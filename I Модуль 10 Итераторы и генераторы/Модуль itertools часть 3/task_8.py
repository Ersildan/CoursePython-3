from itertools import tee

iters = tee([1, 2, 3], 3)

totals = map(lambda a, b, c: a + b + c, *iters)

print(next(totals))
print(next(totals))