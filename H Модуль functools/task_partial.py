from functools import partial


def multiply(a, b):
    return a * b


double = partial(multiply, 2)
triple = partial(multiply, 3)

# Передавая больше аргументов вызовет ошибку
print(double(5))  # 2 * 5
print(triple(10))  # 3 * 10

multiply_two_and_five = partial(multiply, 2, 5)
print(multiply_two_and_five())   # вызываем уже без аргументов
