regex = r'[a-z]\w[A-Z]\1\2\3'


'''
- первый символ — строчная латинская буква
- второй символ — цифра, любая буква в произвольном регистре или символ нижнего подчеркивания
- третий символ — заглавная латинская буква
- четвертый символ должен совпадать с первым символом
- пятый символ должен совпадать со вторым символом
- шестой символ должен совпадать с третьим символом'''