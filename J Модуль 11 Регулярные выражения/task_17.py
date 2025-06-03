import re

regex = r'\bstepik\b'
txt = 'If you have any issues with Stepik technical performance, contact us at support@stepik.org.'

print(re.findall(regex, txt))