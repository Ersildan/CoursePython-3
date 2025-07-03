import re
import keyword
from re import IGNORECASE

def normaliz(el, string):
    return re.sub(rf'\b{el}\b', r'<kw>', string, flags=IGNORECASE)

txt = input()

for i in keyword.kwlist:
    txt = normaliz(i, txt)
print(txt)
