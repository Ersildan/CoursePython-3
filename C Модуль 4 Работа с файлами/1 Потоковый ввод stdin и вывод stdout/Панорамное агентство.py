import sys

data = [line.strip().split(' / ') for line in sys.stdin]
category = data[-1][0]
del data[-1]
data = list(filter(lambda x: x[1] == category, data))
for i in sorted(data, key=lambda x: (float(x[2]), x[0])):
    print(i[0])
