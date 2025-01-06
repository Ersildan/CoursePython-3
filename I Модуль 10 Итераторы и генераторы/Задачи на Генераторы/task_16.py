from datetime import date, timedelta as td

def dates(start, count=None):
    try:
        if count is None:
            while True:
                yield start
                start = start + td(1, 0, 0)
        else:
            while count != 0:
                yield start
                start = start + td(1, 0, 0)
                count -= 1
    except OverflowError:
        return


generator = dates(date(9999, 1, 7))

for _ in range(348):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

try:
   print(next(generator))
except StopIteration:
    print('Error')