from re import fullmatch

pattern = r'\b(\w+)\1\b'
for el in open(0):
    if fullmatch(pattern, el.rstrip('\n')):
        print(el, end='')
