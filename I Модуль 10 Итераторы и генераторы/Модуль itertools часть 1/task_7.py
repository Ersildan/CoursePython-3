from itertools import repeat

repeater = repeat('bee')

for _ in range(100):
    next(repeater)

print(next(repeater))
print(next(repeater))