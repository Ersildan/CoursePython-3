import calendar
print(*[calendar.isleap(int(input())) for _ in range(int(input()))], sep='\n')
