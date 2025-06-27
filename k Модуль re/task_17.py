from re import findall

def abbreviate(phrase):
    match = findall(r'\b\w?|[A-Z]', phrase)
    return ''.join(match).upper()
