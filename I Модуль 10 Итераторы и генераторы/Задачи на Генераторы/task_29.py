string = 'BEEgeek123'

letters = (char for char in string if char.isalpha())
lowers = (char for char in letters if char.islower())
with_stars = ('*' + char + '*' for char in lowers)

print(*with_stars)
