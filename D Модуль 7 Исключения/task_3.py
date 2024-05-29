numbers = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]

remainders = []

for number in numbers:
    try:
        remainders.append(36 % number)
    except:
        continue
print(remainders)
