from itertools import chain

chain_iter1 = chain.from_iterable(['ABC', 'DEF'])      # передаем список
print(*chain_iter1)

chain_iter2 = chain.from_iterable(enumerate('ABC'))
print(*chain_iter2)

for i in chain.from_iterable(['Timur', '29', 'Male', 'Teacher']):
    print(i, end=' ')
