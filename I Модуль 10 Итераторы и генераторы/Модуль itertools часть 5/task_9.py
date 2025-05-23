from itertools import combinations_with_replacement as c

wallet = [100, 50, 20, 10, 5]
cache = dict()

for re in range(1, 21):
    for num, el in enumerate(c(wallet, r=re)):
        if sum(el) == 100 and el not in cache:
            cache[el] = num

print(len(cache))

