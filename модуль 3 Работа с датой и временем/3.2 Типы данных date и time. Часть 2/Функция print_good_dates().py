from datetime import date

def print_good_dates(dates):
    lst = sorted(list(filter(lambda x: x.year == 1992 and x.day + x.month == 29, dates)))
    print(*[i.strftime("%B %d, %Y") for i in lst], sep='\n')
