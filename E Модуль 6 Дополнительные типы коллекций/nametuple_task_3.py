import csv
from collections import namedtuple

with open('meetings.csv', encoding="utf-8") as file:
    friends = namedtuple('friends', ['surname', 'name', 'meeting_date', 'meeting_time'])

    data = list(csv.reader(file))
    del data[0]

    data_ = list(map(friends._make, data))

    print(data_)