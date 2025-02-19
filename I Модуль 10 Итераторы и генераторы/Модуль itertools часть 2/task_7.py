from itertools import compress

data = 'ABCDEF'
selectors = [True, False, True, False, True, False]

result = compress(data, selectors)
print(list(result))