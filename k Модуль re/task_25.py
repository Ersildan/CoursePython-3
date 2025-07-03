import re

txt = input()

while '(' in txt:
    txt = re.sub(r'(\d+)\((\w+)\)', lambda x: int(x[1]) * x[2], txt)
print(txt)
