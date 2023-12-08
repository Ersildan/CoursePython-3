from datetime import date


def num_of_sundays(y):
    start = date(y, 1, 1)
    end = date(y + 1, 1, 1)
    lst = [_ for _ in range(start.toordinal(), end.toordinal()) if date.fromordinal(_).weekday() == 6]
    return len(lst)

'вызов функции отдельно'