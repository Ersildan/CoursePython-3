def bee():
    for char in 'bee':
        yield char

def geek():
    yield from 'geek'

print(*bee())
print(*geek())