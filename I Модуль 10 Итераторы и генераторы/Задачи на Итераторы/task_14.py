class PowerOf:
    def __init__(self, number, lvl=-1):
        self.number, self.lvl = number, lvl

    def __iter__(self):
        return self

    def __next__(self):
        self.lvl += 1
        return self.number ** self.lvl


power_of_two = PowerOf(2)

print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))