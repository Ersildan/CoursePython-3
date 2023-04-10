'''
Реализуйте функцию get_biggest(), которая принимает один аргумент:
numbers — список целых неотрицательных чисел
Функция должна возвращать наибольшее число, которое можно составить из чисел из списка numbers.
Если список numbers пуст, функция должна вернуть число − 1'''

def get_biggest(lst):
    if len(lst) == 0:
        return -1
    else:
        lst = list(map(str, lst))
        lst = sorted(lst, key= lambda x: x * max([len(i) for i in lst]))[::-1]
        if set(lst) == set('0'):
            return 0
        return ''.join(lst)
