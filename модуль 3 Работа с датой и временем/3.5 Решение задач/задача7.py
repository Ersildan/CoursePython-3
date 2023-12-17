from datetime import timedelta as td, datetime as dt

lst = []
pn = "%d.%m.%Y"
day = dt.strptime(input(), pn).toordinal() # ввод даты, от которой будет счет дней.
lst_7 = [dt.fromordinal(i) for i in range(day + 1, day + 8)] # список из 7 дней от (day+1) 

for i in range(int(input())):
    name, bd = input().rsplit(" ", 1)
    s = dt.strptime(bd, pn)
    for j in lst_7:
        if s.month == j.month and s.day == j.day:
            lst.append([name, j - dt.strptime(bd, pn)])

print(min(lst, key=lambda x: x[1])[0] if len(lst) > 0 else "Дни рождения не планируются")
