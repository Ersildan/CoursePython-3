from datetime import date

total = 0        

while (my_date:= input()) != "end":
    day, month, year = my_date.split(".")
    try:
        date_= date(int(year), int(month), int(day))
        total += 1
        print(f"Корректная")
    except:
        print(f"Некорректная")

print(total)
