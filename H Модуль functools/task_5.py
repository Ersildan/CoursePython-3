from functools import lru_cache

@lru_cache()
def ways(n):
    cache = {}
    if n <= 3: return 1
    if n == 4: return 2
    else: cache[n] = ways(n - 1) + ways(n - 3) + ways(n - 4)
    return cache[n]

print(ways(5))