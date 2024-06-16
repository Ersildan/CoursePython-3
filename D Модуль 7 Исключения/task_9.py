def get_id(names, name):
    if type(name) is not str:
        raise TypeError('Имя не является строкой')
    elif name != name.title() or name.isalpha() is False:
        raise ValueError('Имя не является корректным')
    return len(names) + 1


names = ['Timur', 'Anri', 'Dima', 'Arthur', 'Ruslan']
name = ['E', 'd', 'u', 'a', 'r', 'd']

try:
    print(get_id(names, name))
except TypeError as e:
    print(e)