from functools import wraps

class MaxRetriesException(Exception):
    pass

def retry(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                try: return func(*args, **kwargs)
                except: pass
            raise MaxRetriesException
        return wrapper
    return decorator


@retry(8)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 5:
        raise ValueError
    print('beegeek')


beegeek()

#beegeek