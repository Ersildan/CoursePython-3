from collections import Counter

data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')

data.min_values = lambda: [i for i in data.items() if i[1] == min(data.values())]
data.max_values = lambda: [i for i in data.items() if i[1] == max(data.values())]

print(data.max_values())
print(data.min_values())