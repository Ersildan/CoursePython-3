from itertools import repeat

beegeek = ['bee', 'geek']
repeater = repeat(beegeek)

print(next(repeater))

beegeek = beegeek + ['imposter']

print(next(repeater))