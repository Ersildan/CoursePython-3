from itertools import compress, count

def first_largest(iterator, number):
    return next(compress(count(), (num > number for num in iterator)), -1)

iterator = iter([18, 21, 14, 72, 73, 18, 20])

print(first_largest(iterator, 10))

# return next((i for i, num in enumerate(iterator) if num > number), -1)