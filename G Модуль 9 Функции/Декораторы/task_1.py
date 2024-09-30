def sandwich(func):
    def inner(*args, **kwargs):
        print(f'---- Верхний ломтик хлеба ----')
        x = result = func(*args, **kwargs)
        print(f'---- Нижний ломтик хлеба ----')
        return x
    return inner