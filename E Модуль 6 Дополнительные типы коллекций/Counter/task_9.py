from collections import Counter

money = Counter({'rub': 900, 'eur': 1100, 'usd': 500, 'uah': 990, 'cad': 100, 'jpy': 1120})

print(*money.most_common(3))