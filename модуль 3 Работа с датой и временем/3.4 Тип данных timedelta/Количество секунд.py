from datetime import timedelta, datetime

h, m, s = input().split(':')

print(int(timedelta(hours= int(h), minutes= int(m), seconds= int(s)).total_seconds()))
