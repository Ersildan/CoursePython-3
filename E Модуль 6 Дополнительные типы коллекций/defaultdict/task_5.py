from collections import defaultdict


def flip_dict(d):
    res = defaultdict(list)
    for k, v in d.items():
        for number in v:
            res[number] = res.get(number, []) + [k]
    return res
