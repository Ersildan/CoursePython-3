import sys

lst = [s.strip() for s in sys.stdin]

cache = {}
for word in lst:
    result = cache.get(word)
    if result is None:
        new_word = ''.join(sorted(word))
        cache[word] = new_word
        print(new_word)
    else:
        print(result)