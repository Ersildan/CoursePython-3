from datetime import date

st, en = date(day=1, month=1, year=1), date(day=31, month=12, year=9999)
mon = tue = wed = thu = fri = sat = sun = 0

for i in range(st.toordinal(), en.toordinal() + 1):
    if date.fromordinal(i).day == 13:
        match s := date.fromordinal(i).weekday():
            case 0:
                mon += 1
            case 1:
                tue += 1
            case 2:
                wed += 1
            case 3:
                thu += 1
            case 4:
                fri += 1
            case 5:
                sat += 1
            case 6:
                sun += 1

print(mon, tue, wed, thu, fri, sat, sun, sep='\n')
