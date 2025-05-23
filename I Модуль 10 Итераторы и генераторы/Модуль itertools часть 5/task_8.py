from itertools import combinations as comb

wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
cache = dict()

for re in range(1, len(wallet)):
    c = comb(wallet, r=re)
    for num, el in enumerate(c):
        if sum(el) == 100 and el not in cache:
            cache[el] = num

print(len(cache))