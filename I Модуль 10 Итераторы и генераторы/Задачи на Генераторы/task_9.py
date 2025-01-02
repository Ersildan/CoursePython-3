def beegeek():
    for char in 'bee':
        yield char
    for char in 'geek':
        return char

generator = beegeek()

print(*generator)