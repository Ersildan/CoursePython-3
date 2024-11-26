from functools import wraps

def add_attrs(**kwargs):
    def decorator(func):
        for k, v in kwargs.items():
            func.__dict__[k] = v
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator


@add_attrs(attr1='bee', attr2='geek')
def beegeek():
    return 'beegeek'


print(beegeek.attr1) #bee
print(beegeek.attr2) #geek