from datetime import date, time, datetime

dates = [date(1793, 8, 23), date(1410, 3, 11), date(804, 11, 12), date(632, 6, 4),
         date(295, 1, 23), date(327, 8, 24), date(167, 4, 16), date(229, 1, 24),
         date(1239, 2, 5), date(1957, 7, 14), date(197, 8, 24), date(479, 9, 6)]

times = [time(7, 33, 27), time(21, 2, 10), time(17, 20, 47), time(20, 8, 59),
         time(12, 42, 56), time(15, 9, 57), time(17, 47, 9), time(9, 40, 2),
         time(11, 47, 1), time(17, 27, 10), time(17, 55, 40), time(9, 14, 9)]


print(*sorted([datetime.combine(i, j) for i, j in zip(dates, times)], key=lambda x: x.second), sep='\n')
