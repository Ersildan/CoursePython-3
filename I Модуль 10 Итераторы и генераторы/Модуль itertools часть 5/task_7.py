from itertools import permutations

s = [l for l in input()]

print(*sorted(list("".join(el) for el in set(permutations(s, r=len(s))))), sep="\n")

