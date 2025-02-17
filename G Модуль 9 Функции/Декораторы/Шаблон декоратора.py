import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Выполняется код до вызова декорируемой функции
        value = func(*args, **kwargs)
        # Выполняется код после вызова декорируемой функции
        return value
    return wrapper
