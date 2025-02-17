from itertools import accumulate
import operator

def factorials(n):
    return accumulate(range(1, n + 1), operator.mul)

numbers = factorials(6)

print(*numbers)