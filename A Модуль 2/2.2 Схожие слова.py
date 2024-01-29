def foo(s):
    return [words for words, l in enumerate(s, start = 1) if l in letters]


word = input()
letters = 'ауоыиэяюёе'

key = [i for i, l in enumerate(word, start = 1) if l in letters]

for _ in range(int(input())):
    if key == foo(s:=input()):
        print(s)
