import sys

for line in sys.stdin:
    print(line.strip('\n')[::-1])
