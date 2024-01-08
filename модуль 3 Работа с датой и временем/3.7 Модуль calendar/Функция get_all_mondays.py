import calendar
import datetime


def get_all_mondays(y):
    lst = []
    for i in range(1, 13):
        my_weekday = calendar.monthrange(y, i)[1]
        for j in range(1, my_weekday + 1):
            if calendar.weekday(y, i, j) == 0:
                lst.append(datetime.date(y, i, j))
    return lst
