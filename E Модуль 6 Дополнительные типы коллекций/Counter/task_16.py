from collections import Counter

word = 'stepik'

counter1 = Counter(word)
counter2 = Counter(word * 3)

print(counter1 < counter2)

# True