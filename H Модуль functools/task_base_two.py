from functools import partial

basetwo = partial(int, base=2)

print(basetwo('110'))
print(basetwo('1010'))
print(basetwo('11111'))
