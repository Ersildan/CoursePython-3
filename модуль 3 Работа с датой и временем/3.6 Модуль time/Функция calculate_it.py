import time

def calculate_it(func, *args):
    st = time.perf_counter()
    a = func(*args)
    en = time.perf_counter()
    return a, en - st
