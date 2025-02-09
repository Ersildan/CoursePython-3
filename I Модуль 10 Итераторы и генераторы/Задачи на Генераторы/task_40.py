def with_previous(iterable):
    return ((i,(j for j in i)) for i in iterable)

numbers = [1, 2, 3, 4, 5]

print(*with_previous(numbers))