from datetime import datetime as dt
from collections import Counter

lst = [dt.strptime(input().rsplit(' ', 1)[1], "%d.%m.%Y") for i in range(int(input()))]
lst_= list(filter(lambda x: x[1] == max(Counter(lst).values()), Counter(lst).items()))

if len(lst_) > 1:
    for date in sorted(lst_, key=lambda x: x[0]):
        print(dt.strftime(date[0], "%d.%m.%Y"))
else:
    print(dt.strftime(lst_[0][0], "%d.%m.%Y"))
