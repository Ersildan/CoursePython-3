import csv

with open('writing_test.csv', 'w', encoding='utf-8') as csv_file:
    # создаем writer объект и указываем названия столбцов
    writer = csv.DictWriter(csv_file, fieldnames=['first_col', 'second_col'])
    # записываем первую строку с названиями столбцов
    writer.writeheader()
    # записываем строку с данными
    writer.writerow({'first_col': 'value1', 'second_col': 'value2'})
