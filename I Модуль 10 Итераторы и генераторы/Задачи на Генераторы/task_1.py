def bee():
    yield 'b'
    yield 'e'
    yield 'e'

generator = bee()

print(next(generator))
print(next(generator))
print(next(generator))