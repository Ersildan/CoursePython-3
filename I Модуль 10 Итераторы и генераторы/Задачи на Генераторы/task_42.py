def around(iterable):
    start = None
    it = iter(iterable)
    n = next(it, None) # Получаем первый элемент или None, если iterable пуст

    if n is None: return  # Проверяем, пустой ли список выходим из функции, ничего не генерируя

    for el in it:
        yield start, n, el
        start = n
        n = el

    yield start, n, None # Добавляем последнюю пару

numbers = [1, 2, 3, 4, 5]
print(*around(numbers))