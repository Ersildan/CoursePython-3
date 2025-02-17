from itertools import accumulate
import operator
import functools


def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        return (i-1 for i in value)
    return wrapper

@decorator
def factorials(n):
    return accumulate(range(1, n + 1), operator.mul)

numbers = factorials(6)

print(*numbers)
