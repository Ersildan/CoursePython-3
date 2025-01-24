def ____(start=0, step=1):
    """count()"""
    n = start
    while True:
        yield n
        n += step

def ____(iterable):
    """cycle()"""
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
            yield element

def ____(obj, times=None):
    """repeat()"""
    if times is None:
        while True:
            yield obj
    else:
        for i in range(times):
            yield obj