def all_together(*args):
    return (el for it in args for el in it)


objects = [range(3), 'bee', [1, 3, 5], (2, 4, 6)]
print(*all_together(*objects)) # 0 1 2 b e e 1 3 5 2 4 6
