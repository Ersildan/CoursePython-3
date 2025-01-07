def card_deck(suit):

    card_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
    card_mast = ["пик", "треф", "бубен", "червей"]
    while True:
        for i in card_mast:
            for j in card_values:
                if i != suit:
                    yield f"{j} {i}"


generator = card_deck('треф')
cards = [next(generator) for _ in range(40)]

print(*cards)