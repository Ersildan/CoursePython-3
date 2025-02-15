from itertools import starmap

numbers = [(2, 0, 7, 7), (3, 2, 2), (1, 3, 3, 7), (6, 9)]

print(*starmap(max, numbers))