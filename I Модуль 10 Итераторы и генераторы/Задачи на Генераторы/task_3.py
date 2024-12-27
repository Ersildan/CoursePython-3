def bee():
    for char in 'bee':
        yield char

generator = bee()

next(generator)
next(generator)
next(generator)

print(next(generator))