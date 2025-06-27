from re import findall

txt = input()

match = findall(rf'\W?\b{input()}\b\W?', txt)
print(len(match))
