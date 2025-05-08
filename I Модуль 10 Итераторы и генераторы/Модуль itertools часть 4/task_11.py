from itertools import groupby

grp = groupby(sorted(input().split(), key=lambda x: (len(x), x)), key=len)
for k, v in grp:
    print(f"{k} -> {', '.join(list(v))}")
