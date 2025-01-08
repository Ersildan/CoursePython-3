def bee():
    yield 'b'
    yield 'e'
    yield 'e'

def geek():
    yield from 'geek'

print(*bee()) # b e e
print(*geek()) # g e e k