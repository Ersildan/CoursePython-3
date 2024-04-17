import csv
from collections import namedtuple
from datetime import datetime as dt

with open('meetings.csv', encoding="utf-8") as file:
    friends = namedtuple('friends', ['surname', 'name', 'meeting_date', 'meeting_time'])
    data = list(csv.reader(file))
    del data[0]

    data_ = list(map(friends._make, data))
    data_ = sorted(data_, key=lambda x: dt.strptime(x[2]+x[3], '%d.%m.%Y%H:%M'))

    for i in data_:
        print(f"{i.surname} {i.name}")
