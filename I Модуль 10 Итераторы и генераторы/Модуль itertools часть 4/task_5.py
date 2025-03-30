from itertools import groupby

groups = groupby('aaabbbcccaabb')

key, group = next(groups)

print(key, len(group))