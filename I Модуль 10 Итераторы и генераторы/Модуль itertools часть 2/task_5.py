from itertools import filterfalse

numbers = [1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
words = ['is', 'an', 'of', 'python', 'C#', 'beegeek', 'is']

new_numbers = list(filterfalse(lambda num: num <= 5, numbers))
print(new_numbers)

for word in filterfalse(lambda s: len(s) == 2, words):
    print(word)