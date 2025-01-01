def beegeek():
    for char in 'bee':
        yield char
    for char in 'geek':
        yield char

generator = beegeek()

print(*generator)