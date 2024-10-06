from functools import wraps


def returns_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not isinstance(func(*args, *kwargs), str):
            raise TypeError
        return func(*args, **kwargs)
    return wrapper
