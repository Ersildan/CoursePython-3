def format_bytes(size):
    n = 0
    power_l = {0: 'B', 1: 'KB', 2: 'MB', 3: 'GB'}
    while size > 1024:
        size /= 1024
        n += 1
    return f'{int(round(size, 0))} {power_l[n]}'


with open('files.txt', encoding='utf-8') as file:
    # читаем текст и сохраняем его в lst
    lst = file.read().split('\n')
    lst_dict, group_d = [], dict()
    del lst[-1]
    
    # Список имен для словаря
    name_lst_dict = ['name', 'digit', 'kmg']

    # Создаем список словарей с ключами name digit и kmg в lst_dict
    for i in lst:
        lst_dict.append(dict(zip(name_lst_dict, i.split())))

    # через eval строку меняю на число в lst_dict
    for d in lst_dict:
        if d['kmg'] == 'B':
            d["digit"] = eval(d['digit'])
            continue
        elif d['kmg'] == 'KB':
            d['digit'] = eval(d['digit']) * 1024
            d['kmg'] = 'B'
        elif d['kmg'] == 'MB':
            d['digit'] = eval(d['digit']) * (1024 ** 2)
            d['kmg'] = 'B'
        elif d['kmg'] == 'GB':
            d['digit'] = eval(d['digit']) * (1024 ** 3)

    # Создаем группы в group_d по форматам
    for my_dict in lst_dict:
        key = my_dict['name'].split('.')[1]
        group_d.setdefault(key, []).append(my_dict)

    for k, v in sorted(group_d.items()):
        Summary = sum([i['digit'] for i in v])
        for i in sorted(v, key=lambda x: x['name']):
            print(i['name'])
        print('-' * 10)
        print(f'Summary: {format_bytes(Summary)}')
        print()
