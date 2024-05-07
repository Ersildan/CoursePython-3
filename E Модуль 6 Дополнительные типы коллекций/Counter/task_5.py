from collections import Counter


def foo(prod):
    total = 0
    for i in prod.replace(' ', ''):
        total += ord(i)
    return int(total)


product = Counter(input().split(','))
mx = len(max(product, key=lambda x: len(x)))

for k, v in sorted(product.items()):
    print(f"{k.ljust(mx)}: {foo(k)} UC x {v} = {foo(k) * v} UC")
