def simple_sequence():
    total = 1
    while True:
        for i in range(total):
            yield total
        total += 1


generator = simple_sequence()
numbers = [next(generator) for _ in range(10)]

print(*numbers) # 1 2 2 3 3 3 4 4 4 4