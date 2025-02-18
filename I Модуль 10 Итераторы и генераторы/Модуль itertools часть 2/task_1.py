from itertools import dropwhile


# Как только будет получено ложное значение, сгенерирует элементы из итерируемого объекта
numbers = [1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
words = ['is', 'an', 'of', 'python', 'C#', 'beegeek', 'is']

new_numbers = list(dropwhile(lambda num: num <= 5, numbers))
print(new_numbers)

for word in dropwhile(lambda s: len(s) == 2, words):
    print(word)