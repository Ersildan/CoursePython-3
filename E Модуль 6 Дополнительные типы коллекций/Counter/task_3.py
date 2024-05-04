from collections import Counter

products = Counter(input().split(','))

print(*[f"{i[0]}: {i[1]}" for i in sorted(products.items())], sep='\n')
