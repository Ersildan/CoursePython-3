def verification(login, password, success, failure):
    def success(login):
        pass


    def failure(login):
        # Не прошел проверку
        pass


d = {'0': 'в пароле нет ни одной буквы',
     '1': 'в пароле нет ни одной заглавной буквы',
     '2': 'в пароле нет ни одной строчной буквы',
     '3': 'в пароле нет ни одной цифры'}

print(d)
