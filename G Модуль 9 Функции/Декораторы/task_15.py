import functools

def takes(*datatypes):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if all([isinstance(i, datatypes) for i in [*args, *kwargs.values()]]):
                return func(*args, **kwargs)
            else:
                raise TypeError
        return wrapper
    return decorator


@takes(list, int, tuple, str)
def add(a, b):
    '''add docs'''
    return a + b

print(add.__name__)
print(add.__doc__)

try:
    print(add(a='a', b='c'))
except TypeError as e:
    print(type(e))