from itertools import tee

iter1, iter2 = tee([1, 'a', 2, 'b', 3, 'c'])    # по умолчанию n=2

print(*iter1)
print(*iter2)
