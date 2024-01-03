import calendar

y, m = map(int, input().split())
print(calendar.monthrange(y, m)[1])
