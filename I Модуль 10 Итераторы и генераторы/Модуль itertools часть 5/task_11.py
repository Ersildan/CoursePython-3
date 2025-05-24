from itertools import product

numbers = [1, 2]
letters = ['x', 'y', 'z']
flags = [False, True]

print(list(product(numbers, letters)))
print(list(product(letters, numbers)))
print(list(product(letters, numbers, flags)))
