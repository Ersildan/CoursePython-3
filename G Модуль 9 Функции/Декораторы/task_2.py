def decor(func):
    def wrapper(*args, **kwargs):
        new_args = (str(el).upper() for el in args)
        new_kwargs = {k: str(v).upper() for k,v in kwargs.items()}
        func(*new_args, **new_kwargs)
    return wrapper


print = decor(print)
