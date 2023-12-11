from datetime import date, time, datetime, timedelta

data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]

pn = '%H:%M'
x = timedelta(seconds=0)

for i in data:
    x += datetime.strptime(i[1], pn) - datetime.strptime(i[0], pn)

print(int(x.total_seconds()/60))
