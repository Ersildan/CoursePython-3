def interleave(*args):
    return (el for it in zip(*args) for el in it)

print(*interleave('bee', '123'))
