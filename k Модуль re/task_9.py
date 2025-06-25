from re import search

t = 0
for el in open(0):
    if search(r'^(beegeek).*\1$', el):
        t += 3
    else:
        if search(r'^(beegeek).*|(beegeek)$', el):
            t += 2
        elif search(r'.+beegeek.+', el):
            t += 1
print(t)