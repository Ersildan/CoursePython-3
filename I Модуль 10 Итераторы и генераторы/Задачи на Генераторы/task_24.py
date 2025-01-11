def cubes_of_odds(iterable):
    return (number ** 3 for number in iterable if number % 2)


print(*cubes_of_odds([1, 2, 3, 4, 5])) # 1 27 125