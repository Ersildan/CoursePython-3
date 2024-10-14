from functools import partial

def add(a, b):
    return a + b

add_one = partial(add, 1)
add_two = partial(add, 2)

print(add_one(9))
print(add_two(18))