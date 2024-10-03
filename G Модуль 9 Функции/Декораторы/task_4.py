def reverse_args(func):
    def wrapper(*args, **kwargs):
        return func(*args[::-1], **kwargs)
    return wrapper