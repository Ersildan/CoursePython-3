from itertools import groupby

groups = groupby('aaabbbcccaabb')

key1, group1 = next(groups)
key2, group2 = next(groups)

print(key1, list(group1))