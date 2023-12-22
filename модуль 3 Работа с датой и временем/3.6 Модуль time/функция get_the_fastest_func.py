import time

def foo(i, arg):
    st = time.perf_counter()
    a = i(arg)
    en = time.perf_counter()
    return (en - st)
        
def get_the_fastest_func(func, arg):
    return min(func, key=lambda x: foo(x, arg))
    
