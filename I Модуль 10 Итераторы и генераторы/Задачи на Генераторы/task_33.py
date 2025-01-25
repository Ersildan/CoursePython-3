def filter_names(names, ignor_char, max_names):
    lst = (i for i in names if i.lower()[0] != ignor_char.lower() and any(j.isdigit() for j in i) == False)
    yield from (el for ind, el in enumerate(lst) if ind < max_names)




data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 'D', 3))
