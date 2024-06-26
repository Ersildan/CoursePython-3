class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass


def is_good_password(s):
    l_ENG_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l_ENG_lower = l_ENG_upper.lower()

    l_RUS_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    l_RUS_lower = l_RUS_upper.lower()

    if len(s) < 9:
        raise LengthError

    if not any([all([any(_ in l_ENG_upper for _ in s), any(_ in l_ENG_lower for _ in s)]),
           all([any(_ in l_RUS_upper for _ in s), any(_ in l_RUS_lower for _ in s)])]):
        raise LetterError
    if not any(i.isdigit() for i in s):
        raise DigitError

    return True


try:
    print(is_good_password('123456789a'))
except Exception as err:
    print(type(err))
