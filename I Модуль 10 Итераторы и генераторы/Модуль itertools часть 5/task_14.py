from itertools import product

numbers = (
           '0', '1', '2', '3', '4', '5', '6',
           '7', '8', '9', 'A', 'B', 'C', 'D',
           'E', 'F'
           )

n, m = int(input()), int(input())
for el in product(numbers[:n], repeat = m):
    print("".join(el), end=' ')
