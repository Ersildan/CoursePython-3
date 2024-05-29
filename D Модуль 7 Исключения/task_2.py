food = ['chocolate', 'chicken', 'corn',
        'sandwich', 'soup', 'potatoes',
        'beef', 'lox', 'lemonade']
fifth = []

for x in food:
    try:
        fifth.append(x[4])
    except:
        fifth.append('_')
print(fifth)
