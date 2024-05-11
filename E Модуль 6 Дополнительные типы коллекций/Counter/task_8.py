from collections import Counter

money = Counter({'rub': 1000, 'eur': 2000, 'usd': 2000, 'uah': 1900, 'cad': 2100})

print(*money.most_common())