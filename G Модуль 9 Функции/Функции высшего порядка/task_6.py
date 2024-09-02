def verification(login, password, success, failure):
    ALF = "abcdefghijklmnopqrstuvwxyz"
    if any([i.isalpha() and i.lower() in ALF for i in password]): flag1 = True
    else: flag1 = False

    if any([i in ALF.upper() for i in password]): flag2 = True
    else: flag2 = False

    if any([i in ALF for i in password]): flag3 = True
    else: flag3 = False

    if any([i.isdigit() for i in password]): flag4 = True
    else: flag4 = False

    lst = [flag1, flag2, flag3, flag4]
    total = 0

    for i in lst:
        if i == False:
            key = total
            break
        else:
            total += 1

    d = {0: 'в пароле нет ни одной буквы',
         1: 'в пароле нет ни одной заглавной буквы',
         2: 'в пароле нет ни одной строчной буквы',
         3: 'в пароле нет ни одной цифры'}

    if all(lst):
        return success(login)
    else:
        for i in lst:
            if i == False:
                return failure(login, d[key])
