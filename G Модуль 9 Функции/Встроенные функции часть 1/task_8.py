def my_pow(number):
    return sum([int(i)**k for k, i in enumerate(str(number), 1)])
