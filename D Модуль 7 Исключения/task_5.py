import calendar as c

txt = input()

try:
    txt = int(txt)
    if 1 <= txt <= 12:
        print(list(c.month_name)[txt])
    else:
        print('Введено число из недопустимого диапазона')
except:
    print('Введено некорректное значение')
