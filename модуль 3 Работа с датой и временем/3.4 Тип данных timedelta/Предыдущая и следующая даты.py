from datetime import timedelta, datetime

my_date = datetime.strptime(input(), "%d.%m.%Y")
yesterday = my_date - timedelta(days=1)
tomorrow =  my_date + timedelta(days=1)

print(datetime.strftime(yesterday, "%d.%m.%Y"), datetime.strftime(tomorrow, "%d.%m.%Y"), sep='\n')
