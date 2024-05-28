from collections import ChainMap

def get_all_values(chainmap, key):
    s = set()
    [s.add(i[key]) for i in chainmap.maps if key in i and i[key] not in s]
    return s


chainmap = ChainMap({'name': 'Anri'}, {'name': 'Arthur', 'age': 20}, {'name': 'Timur', 'age': 29})
result = get_all_values(chainmap, 'age')

print(*sorted(result))