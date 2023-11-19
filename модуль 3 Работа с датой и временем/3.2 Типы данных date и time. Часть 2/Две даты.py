from datetime import date

d1, d2 = date.fromisoformat(input()), date.fromisoformat(input())

print(min(d1, d2).strftime('%d-%m (%Y)'))
