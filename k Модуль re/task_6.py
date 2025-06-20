from re import fullmatch

for el in open(0):
    if fullmatch('_\d+[a-zA-Z]*_?', el.rstrip('\n')):
        print(True)
    else:
        print(False)
