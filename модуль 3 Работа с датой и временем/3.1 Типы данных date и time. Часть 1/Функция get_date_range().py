from datetime import date

def get_date_range(start, end):
    if date.toordinal(end) < date.toordinal(start):
        return []
    else:
        return [date.fromordinal(i) for i in range(date.toordinal(start), date.toordinal(end) + 1)]
