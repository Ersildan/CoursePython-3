from collections import Counter
import sys

lst = list(map(str.strip, sys.stdin))
d = dict((k, int(v)) for k, v in (i.split() for i in lst))

print(Counter(d).most_common()[-2][0])
