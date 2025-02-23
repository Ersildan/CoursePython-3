from itertools import chain

chain_iter1 = chain('ABC', 'DEF')
print(*chain_iter1)

chain_iter2 = chain(enumerate('ABC'))
print(*chain_iter2)

for i in chain([1, 2, 3], ['a', 'b', 'c'], ('Timur', 29, 'Male', 'Teacher')):
    print(i, end=' ')
