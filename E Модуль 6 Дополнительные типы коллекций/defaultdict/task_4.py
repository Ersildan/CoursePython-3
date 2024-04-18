from collections import defaultdict


def wins(lst):
    res = defaultdict(set)
    for k, v in lst:
        res[k].add(v)
    return res


result = wins([('Тимур', 'Артур'), ('Тимур', 'Дима'), ('Дима', 'Артур')])

for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))
