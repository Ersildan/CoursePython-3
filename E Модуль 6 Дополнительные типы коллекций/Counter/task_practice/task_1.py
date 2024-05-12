from collections import Counter

txt = Counter(input().lower().split()).most_common()[::-1]
lst = list(filter(lambda x: x[1] == txt[0][1], txt))
new_lst = sorted([i[0] for i in lst])

print(", ".join(new_lst))
