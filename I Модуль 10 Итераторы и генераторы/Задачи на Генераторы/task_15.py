def reverse(sequence):
    for el in sequence[::-1]:
        yield el

print(*reverse([1, 2, 3, 4, 5]))