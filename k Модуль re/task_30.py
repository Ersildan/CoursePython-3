import re

def multiple_split(string, delimiters):
    pattern = "|".join([re.escape(el) for el in delimiters])
    return re.split(rf'{pattern}', string)

print(multiple_split('timur.^[+arthur.^[+dima.^[+anri.^[+roma.^[+ruslan', ['.^[+']))

# ['timur', 'arthur', 'dima', 'anri', 'roma', 'ruslan']