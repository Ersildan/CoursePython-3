from datetime import datetime

with open("diary.txt", encoding="UTF-8") as f:
    lst = f.read().split('\n\n')
    lst_ = sorted(lst, key=lambda x: datetime.strptime(x.split('\n')[0], '%d.%m.%Y; %H:%M'))

for row in lst_:
    print(row, end='\n\n')
