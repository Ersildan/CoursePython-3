from collections import Counter

with open('pythonzen.txt', encoding="UTF-8") as file:
    txt = file.read().lower()
    c = list(filter(lambda x: x[0].isalpha() is True, sorted(Counter(txt).items())))
    print(*[f"{i[0]}: {i[1]}" for i in c], sep='\n')
