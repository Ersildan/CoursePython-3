import string
from itertools import cycle

def alnum_sequence():
    return (char for obj in zip(cycle(range(1,27)), cycle(string.ascii_uppercase)) for char in obj)

alnum = alnum_sequence()

print(*(next(alnum) for _ in range(55)))

