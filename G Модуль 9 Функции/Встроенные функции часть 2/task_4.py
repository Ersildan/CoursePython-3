f = input()
a, b = map(int, input().split())
lst = [eval(f) for x in range(a, b + 1)]
print(f'Минимальное значение функции {f} на отрезке [{a}; {b}] равно {min(lst)}')
print(f'Максимальное значение функции {f} на отрезке [{a}; {b}] равно {max(lst)}')