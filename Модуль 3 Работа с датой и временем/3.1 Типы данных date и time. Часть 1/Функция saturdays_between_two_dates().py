from datetime import date

def saturdays_between_two_dates(start, end):
    start, end = min(start, end), max(start, end)
    return len([i for i in range(start.toordinal(), end.toordinal() + 1) if date.fromordinal(i).weekday() == 5])
