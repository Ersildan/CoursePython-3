class Cycle:
    def __init__(self, iterable):
        self.interable = iterable
        self.inter_obj = iter(el for el in self.interable)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.inter_obj)
        except:
            self.inter_obj = iter(el for el in self.interable)
            return next(self.inter_obj)


cycle = Cycle([1])

print(next(cycle) + next(cycle) + next(cycle))