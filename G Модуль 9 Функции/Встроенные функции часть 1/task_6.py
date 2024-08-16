def custom_isinstance(l, t):
    return len(list(filter(lambda x: x, [isinstance(i, t) for i in l])))