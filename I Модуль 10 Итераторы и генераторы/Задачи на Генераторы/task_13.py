def alternating_sequence(count=None):
    if count is None:
        total = 1
        while True:
            if total % 2 == 1:
                yield total
            else:
                yield total * (-1)
            total += 1
    if isinstance(count, int):
        for num in range(1, count + 1):
            if num % 2 == 1:
                yield num
            else:
                yield num * (-1)

generator = alternating_sequence(10)

print(*generator)

