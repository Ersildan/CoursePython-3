from datetime import datetime, timedelta

dt = datetime.strptime(input(), '%d.%m.%Y %H:%M')
x = timedelta(hours= dt.hour, minutes=dt.minute, seconds=dt.second)
check = dt.weekday()

td_start, td_start_ = timedelta(hours=9), timedelta(hours=10)
td_end, td_end_ = timedelta(hours=21), timedelta(hours=18)

if 0 <= check <= 4 and td_start <= x < td_end:
    print(int((td_end - x).total_seconds()/60))
elif 4 < check <= 6 and td_start_ <= x < td_end_:
    print(int((td_end_ - x).total_seconds()/60))
else:
    print('Магазин не работает')
