from datetime import date

dates = [date(2010, 9, 28),
         date(2017, 1, 13),
         date(2009, 12, 25),
         date(2010, 2, 27),
         date(2021, 10, 11),
         date(2020, 3, 13),
         date(2000, 7, 7),
         date(1999, 4, 14),
         date(1789, 11, 19),
         date(2013, 8, 21),
         date(1666, 6, 6),
         date(1968, 5, 26)
         ]

d = {
     1: 'Q1', 2: 'Q1', 3: 'Q1', 4: 'Q2',
     5: 'Q2', 6: 'Q2', 7: 'Q3', 8: 'Q3',
     9: 'Q3', 10: 'Q4', 11: 'Q4', 12: 'Q4'
    }

for i in dates:
    print(f"{i.year}-{d[i.month]}")
