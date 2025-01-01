def bee():
    yield 'b'
    yield 'e'
    return 'e'

next(bee())
next(bee())

print(next(bee())) # b