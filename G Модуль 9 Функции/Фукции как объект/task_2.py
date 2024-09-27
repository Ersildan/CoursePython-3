old_print = print


def print(*args, **kwargs):
    caps = tuple(elem.upper() if isinstance(elem, str) else elem for elem in args)
    if kwargs == {}:
        return old_print(*caps)
    else:
        kwargs['end'] = kwargs['end'].upper()
        kwargs['sep'] = kwargs['sep'].upper()
        return old_print(*caps, sep=kwargs['sep'], end=kwargs['end'])
