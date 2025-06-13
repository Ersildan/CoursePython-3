from re import match

match1 = match(r'[Hh]\w+', 'hello, Timur')
match2 = match(r'[Tt]\w+', 'hello, Timur')

print(match1.group() if match1 else None)
print(match2.group() if match2 else None)