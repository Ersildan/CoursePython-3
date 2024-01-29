'''Будем считать, что PIN-код является корректным, если он удовлетворяет следующим условиям:

состоит из 4, 5 или 6 символов
состоит только из цифр (0−9)
не содержит пробелов
'''
# Code
def is_valid(string):
    f = ' ' not in string
    f2 = 4 <= len(string) <= 6
    f3 = string.isdigit()

    return all([f, f2, f3])
        


''' Test#
Sample Input 1:
print(is_valid('4367'))
Sample Output 1:
True

Sample Input 2:
print(is_valid('92134'))
Sample Output 2:
True

Sample Input 3:
print(is_valid('89abc1'))
Sample Output 3:
False

Sample Input 4:
print(is_valid('900876'))
Sample Output 4:
True

Sample Input 5:
print(is_valid('49 83'))
Sample Output 5:
False
'''
