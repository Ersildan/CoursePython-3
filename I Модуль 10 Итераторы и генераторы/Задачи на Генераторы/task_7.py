def bee():
    yield 'b'
    return 'e'
    yield 'e'

generator = bee()

print(list(generator)) # ['b']