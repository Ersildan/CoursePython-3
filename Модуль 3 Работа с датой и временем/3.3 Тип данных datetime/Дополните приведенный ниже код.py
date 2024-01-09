from datetime import datetime

text = 'Уважаемый пациент, доктор готов принять Вас 15.07.2022 в 08:30'

dt = datetime.strptime(text, 'Уважаемый пациент, доктор готов принять Вас %d.%m.%Y в %H:%M')

print(dt)
