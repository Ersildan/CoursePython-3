def palindromes():
    total = 1
    while True:
        if str(total) == str(total)[::-1]: yield total
        total += 1


generator = palindromes()
numbers = [next(generator) for _ in range(30)]

print(*numbers) # 1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99 101 111 121 131 141 151 161 171 181 191 202 212