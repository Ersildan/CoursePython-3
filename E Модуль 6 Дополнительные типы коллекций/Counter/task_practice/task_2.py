from collections import Counter

txt = Counter(input().lower().split())
print(max(txt.items(), key=lambda x: x[1])[0])
