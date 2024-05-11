from collections import Counter

letters1 = Counter(a=1, b=-2, c=3, d=-4)

letters2 = +letters1
letters3 = -letters2

print(letters3)