import functools

def returns(datatype):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            if isinstance(value, datatype):
                return value
            else:
                raise TypeError
        return wrapper
    return decorator


@returns(list)
def append_this(li, elem):
    '''append_this docs'''
    return li + [elem]

print(append_this.__name__)
print(append_this.__doc__)
print(append_this([1, 2, 3], elem=4))