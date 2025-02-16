from itertools import repeat

beegeek = ['bee', 'geek']
repeater = repeat(beegeek)

print(next(repeater))

beegeek.append('imposter')

print(next(repeater))