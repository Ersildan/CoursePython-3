import sys

data = [line for line in sys.stdin if line.strip()[0] == '#']
print(len(data))
