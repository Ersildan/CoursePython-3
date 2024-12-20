class Cycle:
    def __init__(self, iterable):
        self.interable = iterable

    def __iter__(self):
        return self

    def __next__(self):
        k = next(self.interable)
        pass