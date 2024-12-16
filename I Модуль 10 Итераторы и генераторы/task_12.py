class Square:
    def __init__(self, n, total=1):
        self.n = n
        self.total = total

    def __iter__(self):
        return self

    def __next__(self):
        if self.total - self.n == 1:
            raise StopIteration
        else:
            value = self.total ** 2
            self.total += 1
            return value


squares = Square(10)

print(list(squares))
