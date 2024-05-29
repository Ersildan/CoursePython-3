import sys

total = count = 0

for i in list(map(str.strip, sys.stdin)):
    try: total += float(i)
    except: count += 1

if total == int(total):
    total = int(total)

print(total, count, sep='\n')
