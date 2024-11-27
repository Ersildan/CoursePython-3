from functools import wraps

def ignore_exception(*exc):
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            try: return func(*args, **kwargs)
            except exc as e: print(f'Исключение {type(e).__name__} обработано')
            else: raise type(e).__name__
        return wrapper

    return decorator

@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def f(x):
    return 1 / x

f(0)