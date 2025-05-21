from itertools import permutations

numbers = [1, 2, 3, 4]
letters = 'cba'

all_num_permutations = permutations(numbers)
all_let_permutations = permutations(letters)

print(list(all_num_permutations))
print(list(all_let_permutations))


letters = ['a', 'b', 'c']

permutations1 = permutations(letters, r=1)
permutations2 = permutations(letters, r=2)
permutations3 = permutations(letters, r=3)

print(list(permutations1))
print(list(permutations2))
print(list(permutations3))

from itertools import combinations

numbers = [1, 2, 3, 4]

print(list(combinations(numbers, r=1)))
print(list(combinations(numbers, r=2)))
print(list(combinations(numbers, r=3)))
print(list(combinations(numbers, r=4)))