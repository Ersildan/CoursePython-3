from itertools import groupby

def group_anagrams(lst):
    gr = groupby(sorted(lst, key=sorted), key=sorted)
    return (tuple(v) for k, v in gr)

groups = group_anagrams(['evil', 'father', 'live', 'levi', 'book', 'afther', 'boko'])

print(*groups)
