from datetime import datetime, timedelta

lst = []
pn = '%H:%M'

st = datetime.strptime(input(), pn)
et = datetime.strptime(input(), pn)

lesson = timedelta(minutes=45)
timeout = timedelta(minutes=10)

while st + lesson <= et:
    lst.append([st, (st + lesson)])
    st += lesson + timeout
    
for les in lst:
    print(f"{les[0].strftime('%H:%M')} - {les[1].strftime('%H:%M')}")
