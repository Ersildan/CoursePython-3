from itertools import zip_longest

print(*zip([1, 2, 3], ['a', 'b', 'c', 'd', 'e']))
print(*zip_longest([1, 2, 3], ['a', 'b', 'c', 'd', 'e']))                     # fillvalue=None
print(*zip_longest([1, 2, 3], ['a', 'b', 'c', 'd', 'e'], fillvalue='*'))
print(*zip_longest(['a', 'b', 'c', 'd', 'e'], [1, 2, 3], fillvalue=777))
