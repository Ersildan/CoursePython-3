lst = [input() for _ in range(3)]

ru = "АаВСсЕеНКМОоРрТХху"

lst_ru = [i in ru for i in lst]

if True in lst_ru and False in lst_ru:
    print('mix')
elif all(lst_ru) == True:
    print('ru')
else:
    print('en')
