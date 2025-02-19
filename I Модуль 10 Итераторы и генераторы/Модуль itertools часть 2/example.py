from itertools import takewhile
numbers = [1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1]
print(*takewhile(lambda x: x < 5, numbers)) # 1 2 3 4
print('-' * 10)

from itertools import dropwhile
numbers = [1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1]
print(*dropwhile(lambda x: x < 5, numbers)) # 5 5 5 4 3 2 1
print('-' * 10)

from itertools import filterfalse
names = ['Timur', 'Arthur', 'Dima', 'Anri']
print(*filterfalse(lambda name: name.startswith('A'), names)) # Timur Dima
print('-' * 10)

objects = [True, False, 'True', 'False', [], ()]
print(*filterfalse(None, objects)) # False [] ()
print('-' * 10)

from itertools import compress
numbers = [1, -2, 3, 4, -5, -6, 7, 8, -9, -10]
selectors = (i > 0 and i % 2 == 0 for i in numbers)
print(*compress(numbers, selectors)) # 4 8
print('-' * 10)

from itertools import cycle
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
every_third = cycle([False, False, True])
print(*compress(numbers, every_third)) # 3 6 9
print('-' * 10)

from itertools import islice
print(*islice('beegeek', 4)) # b e e g
print('-' * 10)
print(*islice('beegeek', None)) # b e e g e e k
print('-' * 10)
print(*islice('beegeek', 2, 6)) # e g e e
print('-' * 10)
print(*islice('stepik', 0, 6, 2)) # s e i
print('-' * 10)