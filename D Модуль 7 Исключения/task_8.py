import calendar as c
import locale

locale.setlocale(locale.LC_ALL, 'ru-RU.UTF-8')


def get_weekday(number):
    if isinstance(number, int) is not True:
        raise TypeError('Аргумент не является целым числом')
    elif number not in (1, 2, 3, 4, 5, 6, 7):
        raise ValueError('Аргумент не принадлежит требуемому диапазону')
    else:
        print(list(c.day_name)[number - 1].title())


try:
    print(get_weekday([]))
except Exception as err:
    print(err)
    print(type(err))