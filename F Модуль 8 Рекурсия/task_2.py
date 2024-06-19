def foo(n):
    if n < 101:
        print(n)
        foo(n + 1)


foo(1)