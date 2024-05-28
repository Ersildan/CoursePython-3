from collections import ChainMap, Counter

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

products = Counter(input().split(','))
mx = len(max(products, key=len))
d = ChainMap(bread, meat, sauce, vegetables, toppings)
total = 0
global_max = 0
for k, v in sorted(products.items()):
    print(txt := f"{k.ljust(mx)} x {v}")
    total += v * d[k]
    if len(txt) > global_max:
        global_max = len(txt)
global_max = global_max if len(f"ИТОГ: {total}р") < global_max else len(f"ИТОГ: {total}р")
print('-' * global_max)
print(f"ИТОГ: {total}р")
