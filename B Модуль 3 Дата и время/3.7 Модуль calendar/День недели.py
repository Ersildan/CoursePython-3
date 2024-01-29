import calendar
from datetime import date

my_date = date.fromisoformat(input())

print(calendar.day_name[date.weekday(my_date)])
