from functools import partial

def add(a, b):
    return a + b

add_one = partial(add, 1)

print(add_one(2, 3))