class Fibonacci:
    def __init__(self, one=0, two=1):
        self.one = one
        self.two = two

    def __iter__(self):
        return self

    def __next__(self):
        self.one, self.two = self.two, self.one + self.two
        return self.one


fibonacci = Fibonacci()

print(next(fibonacci)) # 1
print(next(fibonacci)) # 1
print(next(fibonacci)) # 2
print(next(fibonacci)) # 3
