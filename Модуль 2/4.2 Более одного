'''Дана последовательность неотрицательных целых чисел. Напишите программу,
которая выводит те числа, которые встречаются в данной последовательности 
более одного раза.'''

numbers = list(map(int, input().split()))

lst = set(list(filter(lambda x: numbers.count(x) > 1, numbers)))

print(*sorted(lst))
