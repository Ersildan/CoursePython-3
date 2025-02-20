def first_true(iterable, predicate):
    return next(filter(predicate, iterable), None)

numbers = [10000]

print(first_true(numbers, lambda num: num % 2 == 1))