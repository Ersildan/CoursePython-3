import sys
import datetime


lst = [datetime.datetime.strptime(i.strip(), '%d.%m.%Y') for i in sys.stdin]

lst_ASC, lst_DESC = [], []
for i in range(len(lst)-1):
    lst_ASC.append(lst[i] < lst[i + 1])
    lst_DESC.append(lst[i] > lst[i + 1])

if all(lst_ASC):
    print('ASC')
elif all(lst_DESC):
    print('DESC')
else:
    print('MIX')