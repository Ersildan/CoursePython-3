def get_all_values(nested_dicts, key):
    s = set()
    for k, v in nested_dicts.items():
        if k == key:
            s.update([v])
        elif isinstance(v, dict):
            value = get_all_values(v, key)
            s.update(value)
    return s


my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
result = get_all_values(my_dict, 'top_grade')

print(*sorted(result))
