from datetime import date, timedelta

d, m, y = map(int, input().split('.'))
my_date = date(y, m, d)
print(date.strftime(my_date, '%d.%m.%Y'))

for i in range(2, 11):
    my_date += timedelta(days= i)
    print(date.strftime(my_date, '%d.%m.%Y'))
