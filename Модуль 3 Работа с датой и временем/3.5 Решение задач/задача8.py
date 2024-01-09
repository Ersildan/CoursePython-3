from datetime import datetime as dt, timedelta as td

def choose_plural(amount, t):
    d = {0: ("день", "дня", "дней"),
         1: ("час", "часа", "часов"),
         2: ("минута", "минуты", "минут")}
    
    variant = 2
    if amount % 10 == 1 and amount % 100 != 11:
        variant = 0
    elif amount % 10 >= 2 and amount % 10 <= 4 and (amount % 100 < 10 or amount % 100 >= 20):
        variant = 1
    return '{} {}'.format(amount, d[t][variant])


dx = dt(day= 8, month= 11, year= 2022, hour=12)
dy = dt.strptime(input(), '%d.%m.%Y %H:%M')

x = dx - dy # all timedelta
xd = x.days # days
xh = x.seconds//3600 # hours
xm = x.seconds//60 % 60 # minutes

if dx <= dy:
    print('Курс уже вышел!')
elif xd > 0 and xh > 0:
    print(f'До выхода курса осталось: {choose_plural(xd, 0)} и {choose_plural(xh, 1)}')
elif xd > 0 and xh == 0:
    print(f'До выхода курса осталось: {choose_plural(xd, 0)}')
elif xd == 0 and xh > 0 and xm > 0:
    print(f'До выхода курса осталось: {choose_plural(xh, 1)} и {choose_plural(xm, 2)}')
elif xd == 0 and xh > 0 and xm == 0:
    print(f'До выхода курса осталось: {choose_plural(xh, 1)}')
elif xd == 0 and xh == 0 and xm > 0:
    print(f'До выхода курса осталось: {choose_plural(xm, 2)}')
