from re import findall

txt = input()

match = findall(rf'\B({input()})\B', txt)
print(len(match))
