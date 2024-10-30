from functools import partial

def add(a, b):
    '''documentation'''
    return a + b

add_one = partial(add, 1)

print(add_one.__name__)
print(add_one.__doc__)