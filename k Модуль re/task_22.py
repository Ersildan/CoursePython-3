import re

def normalize_whitespace(string):
    return re.sub(r'\s+', ' ', string)
