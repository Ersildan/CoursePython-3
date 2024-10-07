from functools import wraps


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        name = func.__name__
        print(f"TRACE: вызов {name}() с аргументами: {args}, {kwargs}")
        print(f"TRACE: возвращаемое значение {name}():", repr(func(*args, **kwargs)))
        return func(*args, **kwargs)
    return wrapper


@trace
def say(name, line):
    return f'{name}: {line}'


say('Jane', 'Hello, World')
