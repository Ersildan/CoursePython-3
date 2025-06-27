from re import findall, IGNORECASE

word, txt = input(), input()

match = findall(rf'\W?\b{word[:-2]}(se|ze)\b\W?', txt, flags=IGNORECASE)
print(len(match))
