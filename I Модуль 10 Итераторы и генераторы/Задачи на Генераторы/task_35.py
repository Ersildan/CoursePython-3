from datetime import date

def years_days(year):
    return (date.fromordinal(day) for day
            in range(date.toordinal(date(year,1,1)), date.toordinal(date(year,12,31)) + 1)
            )


dates = years_days(2022)

print(next(dates))
print(next(dates))
print(next(dates))
print(next(dates))