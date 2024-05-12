from collections import Counter

txt = Counter([len(i) for i in input().lower().split()])
print(*[f"Слов длины {i[0]}: {i[1]}" for i in sorted(txt.items(), key=lambda x: x[1])], sep='\n')
