from itertools import groupby

numbers = [1, 1, 1, 7, 7, 7, 7, 15, 7, 7, 7]

group_iter = groupby(numbers)

print(type(group_iter))
print(*group_iter, sep='\n')
