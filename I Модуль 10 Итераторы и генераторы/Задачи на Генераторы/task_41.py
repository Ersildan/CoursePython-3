def pairwise(iterable):
    it = iter(iterable)
    n = next(it, None) # Получаем первый элемент или None, если iterable пуст

    if n is None: return  # Проверяем, пустой ли список выходим из функции, ничего не генерируя

    for el in it:
        yield n, el
        n = el

    yield n, None # Добавляем последнюю пару


numbers = [1, 2, 3, 4, 5]

print(*pairwise(numbers))