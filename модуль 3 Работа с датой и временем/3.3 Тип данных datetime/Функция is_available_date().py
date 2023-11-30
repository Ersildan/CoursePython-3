from datetime import datetime


def is_available_date(dates, some_date):
    lst = []
    for date in dates:
        if len(date) == 10:
            lst.append(datetime.strptime(date, "%d.%m.%Y").date().toordinal())
        else:
            start_day, end_day = date.split('-')
            a = datetime.strptime(start_day, "%d.%m.%Y").date().toordinal()
            b = datetime.strptime(end_day, "%d.%m.%Y").date().toordinal()
            lst = lst + [_ for _ in range(a, b + 1)]

    if len(some_date) == 10:
        x = datetime.strptime(some_date, "%d.%m.%Y").date().toordinal()
        return True if x not in lst else False
    else:
        start_need_day, end_need_day = some_date.split('-')
        d = datetime.strptime(start_need_day, "%d.%m.%Y").date().toordinal()
        c = datetime.strptime(end_need_day, "%d.%m.%Y").date().toordinal()
        lst_need = [_ for _ in range(d, c + 1)]
        return set(lst).isdisjoint(set(lst_need))
      
