def bee():
    yield 'b'
    yield 'e'
    yield 'e'

print(next(bee()))
print(next(bee()))
print(next(bee()))
