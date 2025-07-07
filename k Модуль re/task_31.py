import re

ps, ed = map(int, input().split())
regex_obj = re.compile(r'\d+')
result = regex_obj.findall(input(), pos = ps, endpos = ed)

print(sum(map(int, result)))
