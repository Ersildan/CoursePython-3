from re import findall, IGNORECASE

word, txt = input(), input()

match = findall(rf'\W?\b{word[:-3]}(our|or)\b\W?', txt, flags=IGNORECASE)
print(len(match))
