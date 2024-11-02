import functools

def strip_range(start, end, char='.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            span = range(start, end)
            value = func(*args, **kwargs)
            return "".join([el if i not in span else char for i, el in enumerate(value)])
        return wrapper
    return decorator


@strip_range(20, 30)
def beegeek():
    return 'beegeek'


print(beegeek())
