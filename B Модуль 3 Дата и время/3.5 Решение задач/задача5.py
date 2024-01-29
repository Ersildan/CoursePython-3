from datetime import datetime as dt

lst = []

for _ in range(int(input())):
    name, birthday = input().rsplit(" ", 1)
    lst.append([name, dt.strptime(birthday, "%d.%m.%Y")])
