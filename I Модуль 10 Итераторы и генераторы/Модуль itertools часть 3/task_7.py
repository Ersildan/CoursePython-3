from itertools import chain

def sum_of_digits(iterable):
    return sum(int(i) for i in chain.from_iterable(map(str, iterable)))

print(sum_of_digits([13, 20, 41, 2, 2, 5]))
