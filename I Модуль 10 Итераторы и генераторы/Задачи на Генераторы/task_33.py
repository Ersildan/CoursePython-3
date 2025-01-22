def filter_names(names, ignor_char, max_names):
    return (
        i for i in names
        if i.lower()[0] != ignor_char
        and
        any(j.isdigit() for j in i) == False
    )

data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 'D', 3))
