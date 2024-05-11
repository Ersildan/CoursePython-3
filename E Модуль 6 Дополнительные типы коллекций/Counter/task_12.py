from collections import Counter

left_pocket = Counter(coin=11, candy=4, key=1)
right_pocket = Counter(coin=19, candy=1, key=2, card=2)

print(left_pocket.total() + right_pocket.total())