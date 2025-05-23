from itertools import combinations

numbers1 = [1, 2, 3]
numbers2 = [3, 2, 1]

combinations1 = set(combinations(numbers1, 2))
combinations2 = set(combinations(numbers2, 2))

print(combinations1 == combinations2)