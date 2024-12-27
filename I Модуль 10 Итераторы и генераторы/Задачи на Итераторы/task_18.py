import random as r

class RandomNumbers:
    def __init__(self, left, right, n):
        self.left = left
        self.right = right
        self.n = n
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        iter_obj = iter(r.randint(self.left, self.right) for _ in range(self.n))
        if self.index != self.n:
            self.index += 1
            return next(iter_obj)
        else:
            raise StopIteration


iterator = RandomNumbers(-1000, -900, 4)

print(next(iterator) in range(-1000, -899))
print(next(iterator) in range(-1000, -899))
print(next(iterator) in range(-1000, -899))
print(next(iterator) in range(-1000, -899))

try:
    next(iterator)
except StopIteration:
    print('Error')