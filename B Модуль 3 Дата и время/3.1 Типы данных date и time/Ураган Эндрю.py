# импортируем тип date из модуля datetime
from datetime import date

# создаем объект, соответсвующий дате урагана
hurricane_andrew = date(1992, 8, 24)

# выводим день недели
print(hurricane_andrew.weekday())
