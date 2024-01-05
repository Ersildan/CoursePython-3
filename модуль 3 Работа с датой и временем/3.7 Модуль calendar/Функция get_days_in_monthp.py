import calendar
import datetime


def get_days_in_month(y, m):
    month_num = list(calendar.month_name).index(m)
    total_day = calendar.monthrange(y, month_num)[1] + 1
    return [datetime.date(y, month_num, i) for i in range(1, total_day)]
