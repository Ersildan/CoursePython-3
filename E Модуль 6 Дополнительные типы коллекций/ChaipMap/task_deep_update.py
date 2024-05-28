from collections import ChainMap


def deep_update(chainmap, key, value):
    if key in chainmap:
        for d in chainmap.maps:
            if key in d:
                d[key] = value
    else:
        chainmap.setdefault(key, value)

chainmap = ChainMap({'name': 'Tanya'}, {'name': 'Arthur'}, {'name': 'Timur'})

deep_update(chainmap, 'name', 'Dima')

print(chainmap)