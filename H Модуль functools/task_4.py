from functools import partial

def add(a, b):
    return a + b

add_one = partial(add, 1)

print(add_one.func.__name__)
print(add_one.func(2, 3))