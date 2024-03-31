txt, txt_ = input(), input().lower()

alf = {chr(i): txt[i-97] for i in range(97, 97 + 26)}

print("".join(alf[i] if i.isalpha() is True else i for i in txt_))


'''
from string import ascii_letters

translator = str.maketrans(ascii_letters, input() * 2)

print(input().translate(translator))

'''