import re
regex = (r'\bcat', r'cat\b', r'\bcat\b', r'\Bcat', r'cat\B', r'\Bcat\B')

s = "Some words contain the word cat: scat, ducati, alcatel, catalyst, worldcat and of course cat!"
for pattern in regex:
    print(len(re.findall(pattern, s)))