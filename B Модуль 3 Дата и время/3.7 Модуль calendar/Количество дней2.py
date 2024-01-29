import calendar

y, m = input().split()

print(calendar.monthrange(int(y), list(calendar.month_name).index(m))[1])
