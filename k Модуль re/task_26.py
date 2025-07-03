import re
pattern = r'\b(\w+)(?:\W+\1\b)+'
print(re.sub(pattern, r'\1', input()))