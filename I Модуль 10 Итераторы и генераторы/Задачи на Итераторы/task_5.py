def get_min_max(data):
    if data:
        return min(enumerate(data), key=lambda x: x[1])[0], max(enumerate(data), key=lambda x: x[1])[0]


iterable = iter(range(10))
print(get_min_max(iterable)) #(0, 9)
