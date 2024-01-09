from datetime import timedelta
from datetime import datetime as dt

pn = "%d.%m.%Y"
st = dt.strptime(input(), pn)
en = dt.strptime(input(), pn)

for i in range(st.toordinal(), en.toordinal() + 1):
    my_date = dt.fromordinal(i)
    if (my_date.month + my_date.day) % 2 == 1:
        start_date = dt.fromordinal(i)
        break
        
for i in range(start_date.toordinal(), en.toordinal() + 1, 3):
    I = dt.fromordinal(i)
    if I.weekday() != 0 and I.weekday() != 3:
        print(dt.strftime(I, "%d.%m.%Y"))
