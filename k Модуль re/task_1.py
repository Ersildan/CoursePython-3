from re import search

match1 = search(r'\w+', 'Hello, Timur')

print(match1.group() if match1 else None)
