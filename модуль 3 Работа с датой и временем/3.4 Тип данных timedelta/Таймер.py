from datetime import timedelta, datetime

t = datetime.strptime(input(), "%H:%M:%S")
td = t + timedelta(seconds=int(input()))

print(td.time())
