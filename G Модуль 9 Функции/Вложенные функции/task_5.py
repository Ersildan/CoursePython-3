def sort_priority(values, group):
    values[:] = sorted(values, key=lambda x: x if x in group else x + max(values) + max(group))


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {5, 7, 2, 3}
sort_priority(numbers, group)

print(numbers)