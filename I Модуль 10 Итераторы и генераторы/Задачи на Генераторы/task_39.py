def stop_on(iterable, obj):
    it = iter(iterable)
    return iter(lambda: next(it), obj)


iterator = iter('beegeek')

print(*stop_on(iterator, 'a'))
