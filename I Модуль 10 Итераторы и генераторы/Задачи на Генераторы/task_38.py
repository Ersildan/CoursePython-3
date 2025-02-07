from collections import Counter

def unique(iterable):
    return iter(Counter(iterable))

iterator = iter('111222333')
uniques = unique(iterator)

print(next(uniques))
print(next(uniques))
print(next(uniques))
