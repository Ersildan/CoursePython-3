def bee():
    yield 'b'
    yield 'e'
    return 'e'

generator = bee()

next(generator)
next(generator)

print(next(generator)) # Error