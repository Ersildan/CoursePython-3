def zip_longest(*args, fill=None):
    max_len = len(max(args, key=len))
    a = map(lambda x: x + [fill] * (max_len - len(x)), args)
    return list(zip(*a))
