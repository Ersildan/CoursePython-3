def nonempty_lines(file):
    with open(file, encoding='UTF-8') as f:
        lines = (line.strip() if len(line) <= 25 else '...'  for line in f.readlines() if len(line.strip()) != 0)
    return lines

lines = nonempty_lines('file1.txt')

print(next(lines))
print(next(lines))
print(next(lines))
print(next(lines))
