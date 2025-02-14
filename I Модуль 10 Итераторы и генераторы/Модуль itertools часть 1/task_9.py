from itertools import starmap

pairs = [(2, 2), (3, 2), (1, 4)]

print(*starmap(pow, pairs))