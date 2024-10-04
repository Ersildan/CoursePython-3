def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs), 'Функция выполнилась без ошибок',)
        except:
            return f"(None, 'При вызове функции произошла ошибка')"
    return wrapper
