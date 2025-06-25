from re import search

t1 = t2 = 0
for el in open(0):
    if search(r'bee.*bee', el.rstrip('\n')): t1 += 1
    if search(r'\bgeek\b', el.rstrip('\n')): t2 += 1
print(t1, t2, sep='\n')

'''Напишите программу, определяющую:

количество строк, в которых bee встречается в качестве подстроки не менее двух раз
количество строк, в которых geek встречается в качестве слова хотя бы один раз'''

#test1
'''
beebee bee
beegeek
bee geek bee'''
# 2 - Первый паттерн
# 1 - Второй паттерн