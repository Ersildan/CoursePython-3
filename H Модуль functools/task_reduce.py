from functools import reduce


def foo(x, y) -> int:
    return x + y


print(reduce(foo, [1, 2, 3, 5]))
