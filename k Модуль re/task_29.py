import re

lst = re.split(r'\s*\|\s*|\s*&\s*|\s*and\s*|\s*or\s*', input())
print(", ".join(lst))


'''
import re

print(*re.split(r'\s*(?:[&|]|and|or)\s*', input()), sep=', ')

'''