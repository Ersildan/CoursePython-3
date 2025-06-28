import re
def func(match_obj):
    s = match_obj.group(0)         # строка совпадения
    if s.isdigit():
        return str(int(s) * 10)
    else:
        return s.upper()

result = re.sub(r'\w+', func, r'foo.10.bar.20.baz30.40')

print(result)