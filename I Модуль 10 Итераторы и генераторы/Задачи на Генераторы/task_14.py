def primes(left, right):
    for i in range(left, right + 1):
        if i == 1:
            continue
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i


generator = primes(1, 15)

print(*generator)  #2 3 5 7 11 13