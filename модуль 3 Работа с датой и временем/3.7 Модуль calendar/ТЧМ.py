import calendar

y = int(input())

lst = []
for i in range(1, 13):
    my_weekday = calendar.monthrange(y, i)[1]
    total = 0
    for j in range(1, my_weekday + 1):
        if calendar.weekday(y, i, j) == 3:
            total += 1
        if calendar.weekday(y, i, j) == 3 and total == 3:
            lst.append(f"{j}.{str(i).zfill(2)}.{y}")

print(*lst, sep="\n")
