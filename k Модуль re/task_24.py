import re

print(re.sub(r'(\w)(\w)(\w*)', r'\2\1\3', input()))
