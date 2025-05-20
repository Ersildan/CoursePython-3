from itertools import groupby

def ranges(numbers):
    gr = groupby(sorted(numbers), key=lambda x: numbers.index(x) - x)
    result = []
    for k, v in gr:
        lst = list(v)
        if len(lst) == 1:
            result.append((lst[0], lst[0]))
        else:
            result.append((lst[0], lst[-1]))
    return result

numbers = [1, 2, 3, 4, 7, 8, 10]

print(ranges(numbers))