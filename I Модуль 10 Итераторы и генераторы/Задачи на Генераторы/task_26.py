def count_iterable(iterable):
    return sum(1 for i in iterable)


numbers = iter([1, 2, 3, 4, 5, 6, 7])

print(count_iterable(numbers)) # 7