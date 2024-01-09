import calendar

y, m = input().split()
calendar.prmonth(int(y), list(calendar.month_abbr).index(m))
