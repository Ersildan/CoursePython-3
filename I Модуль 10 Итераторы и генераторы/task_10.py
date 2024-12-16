def is_iterator(obj):
    try: next(obj); return True
    except: return False

beegeek = filter(None, [0, 0, 1, 1, 0, 1])

print(is_iterator(beegeek))
