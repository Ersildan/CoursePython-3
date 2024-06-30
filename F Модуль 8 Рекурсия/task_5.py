def bee(n, s):
    if n < 4:
        print((str(n) * int(s)).center(16))
        bee(n + 1, s - 4)
    print((str(n) * int(s)).center(16))


bee(1, 16)
