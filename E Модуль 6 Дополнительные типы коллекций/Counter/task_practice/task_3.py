from collections import Counter

txt = Counter(input().lower().split()).most_common()

print(max(txt, key=lambda x: (x[1], x[0]))[0])
