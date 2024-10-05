import functools

def square(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)**2
    return wrapper


@square
def add(*args, **kwargs):
    return sum([*args, *kwargs.values()])

print(add(3, 7, x=10, y=30))