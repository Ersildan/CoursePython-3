import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Что-то выполняется до вызова декорируемой функции
        value = func(*args, **kwargs)
        # декорируется возвращаемое значение функции
        # или что-то выполняется после вызова декорируемой функции
        return value
    return wrapper