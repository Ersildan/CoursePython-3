def bee():
    print('--')
    yield 'b'
    yield 'e'
    yield 'e'
    print('--')

for elem in bee():
    print(elem)

    