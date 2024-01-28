import sys

for line in sys.stdin:
    if (line.lstrip(' ')[0] != '#'):
        print(line.rstrip('\n'))
