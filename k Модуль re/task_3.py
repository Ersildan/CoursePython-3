from re import fullmatch

match1 = fullmatch(r'[Hh]\w+ [Tt]\w+', 'Hello, Timur')
match2 = fullmatch(r'[Hh]\w+, [Tt]\w+', 'Hello, Timur')

print(match1.group() if match1 else None)
print(match2.group() if match2 else None)