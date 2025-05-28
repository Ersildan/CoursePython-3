import re

text = input()
pattern = r'7-\d{3}-\d{3}-\d{2}-\d{2}|8-\d{3}-\d{4}-\d{4}'
matches = re.findall(pattern, text)

for mat in matches:
    print(mat)

# Перезвони мне, пожалуйста: 7-919-667-21-19