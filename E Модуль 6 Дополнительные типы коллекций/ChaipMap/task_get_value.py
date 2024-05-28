from collections import ChainMap


def get_value(chainmap, key, from_left=True):
    lst = chainmap.maps

    if from_left == False:
        lst = lst[::-1]

    for d in lst:
        if key in d:
            return d[key]
        else:
            continue


chainmap = ChainMap({'age': 20}, {'city': 'Moscow'}, {'name': 'Anri', 'age': 20}, {'name': 'Timur', 'age': 29})

print(get_value(chainmap, 'age', False))