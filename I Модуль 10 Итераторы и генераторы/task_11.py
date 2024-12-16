import random


def random_numbers(left, right):
    zero_iterator = iter(lambda: random.randint(left, right ), -1)
    return zero_iterator

iterator = random_numbers(1, 10)

print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
