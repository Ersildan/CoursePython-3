from re import search, IGNORECASE

total = 0
for el in open(0):
    match = search('.?beegeek.?', el, flags=IGNORECASE)
    if match: total += 1
print(total)