def takes_positive(func):
    def wrapper(*args, **kwargs):
        lst = [*args, *kwargs.values()]
        if all([isinstance(el, int) and el > 0 for el in lst]):
            return func(*args, **kwargs)
        elif all([isinstance(el, int) for el in lst]) == False:
            raise TypeError
        else:
            raise ValueError
    return wrapper


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(10, 20, 16, 18, '10'))
except Exception as err:
    print(type(err))