import pickle


def foo(check):
    if len(check) == 0:
        return 0
    else:
        return min(check) * max(check)


with open(input(), 'rb') as file:
    n = int(input())
    data = pickle.load(file)

    text = ('Контрольные суммы не совпадают', 'Контрольные суммы совпадают')

    if type(data) is list:
        print(text[foo(list(filter(lambda x: type(x) is int, data))) == n])
    else:
        print(text[sum([_[0] for _ in list(filter(lambda x: type(x[0]) is int, data.items()))]) == n])
