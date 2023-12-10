from datetime import datetime

lst = [datetime.strptime(_, "%d.%m.%Y") for _ in input().split()]
lst_= [abs(lst[i] - lst[i + 1]).days for i in range(0, len(lst) - 1)]

print(lst_)
