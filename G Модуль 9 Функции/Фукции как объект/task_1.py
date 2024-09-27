def numbers_sum(elems):
    """Принимает список и возвращает сумму его чисел (int, float),
игнорируя нечисловые объекты. 0 - если в списке чисел нет."""
    lst = sum(list(filter(lambda x: isinstance(x, (int, float)) == True, elems)))
    return 0 if lst == 0 else lst