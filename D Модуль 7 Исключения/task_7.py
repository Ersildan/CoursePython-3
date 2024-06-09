try:
    with open(input(), encoding='UTF-8') as file:
            print(file.read())
except:
    print('Файл не найден')