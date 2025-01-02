def bee():
    yield 'b'
    print('--')
    yield 'e'
    print('--')
    yield 'e'

for elem in bee():
    print(elem)