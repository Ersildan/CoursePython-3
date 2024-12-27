class Xrange:
    def __init__(self, start, end, step=1):

        if all([isinstance(el, int) for el in (start, end, step)]):
            self.start = start
            self.end = end
            self.step = step
            self.data = iter(i for i in range(self.start, self.end, self.step))
        else:
            self.start = int(start * 100)
            self.end = int(end * 100)
            self.step = int(step * 100)
            self.data = iter(i / 100 for i in range(self.start, self.end, self.step))

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.data)
        except:
            raise StopIteration

evens = Xrange(0, 10, 2)

print(*evens) # 0 2 4 6 8