from datetime import datetime as dt, timedelta as td

dx = dt(day= 8, month= 11, year= 2022, hour=12)
dy = dt.strptime(input(), '%d.%m.%Y %H:%M')

x = dx - dy
xts = x.total_seconds()
xdays = xts / 86400
xhours = xts / 1200
xminutes = xts / 60

print(xdays)
print(xhours)
