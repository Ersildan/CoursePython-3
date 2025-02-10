def with_previous(iterable):
    return (i for i in iterable)

numbers = [1, 2, 3, 4, 5]

print(*with_previous(numbers))