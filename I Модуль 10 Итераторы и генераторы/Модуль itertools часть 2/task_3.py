from itertools import takewhile

numbers = [1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
words = ['is', 'an', 'of', 'python', 'C#', 'beegeek', 'is']

new_numbers = list(takewhile(lambda num: num <= 5, numbers))
print(new_numbers)

for word in takewhile(lambda s: len(s) == 2, words):
    print(word)