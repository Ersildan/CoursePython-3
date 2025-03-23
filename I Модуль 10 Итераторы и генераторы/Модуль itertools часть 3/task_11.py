from itertools import pairwise

def max_pair(iterable):
    return max(el[0] + el[1] for el in pairwise(iterable))

iterator = iter([5, 6, 4, 3, 2, 2])

print(max_pair(iterator))