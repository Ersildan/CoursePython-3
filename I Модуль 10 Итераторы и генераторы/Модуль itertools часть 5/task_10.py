from collections import namedtuple
from itertools import combinations as comb

Item = namedtuple('Item', ['name', 'mass', 'price'])

items = [Item('Обручальное кольцо', 7, 49_000),
         Item('Мобильный телефон', 200, 110_000),
         Item('Ноутбук', 2000, 150_000),
         Item('Ручка Паркер', 20, 37_000),
         Item('Статуэтка Оскар', 4000, 28_000),
         Item('Наушники', 150, 11_000),
         Item('Гитара', 1500, 32_000),
         Item('Золотая монета', 8, 140_000),
         Item('Фотоаппарат', 720, 79_000),
         Item('Лимитированные кроссовки', 300, 80_000)]
lst = []
num = int(input())

for re in range(1, len(items) + 1):
    c = comb(sorted(filter(lambda x: x[1] <= num, items), key=lambda x: x[0]), r=re)
    for j in c:
        if sum(map(lambda x: x.mass, j)) <= num:
            lst.append(j)

if len(lst) == 0:
    print('Рюкзак собрать не удастся')
else:
    print(*(el.name for el in max(lst, key=lambda x: sum(i.price for i in x))), sep="\n")