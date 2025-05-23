from itertools import permutations

numbers1 = [1, 2, 3]
numbers2 = [3, 2, 1]

permutations1 = set(permutations(numbers1))
permutations2 = set(permutations(numbers2))

print(permutations1 == permutations2)