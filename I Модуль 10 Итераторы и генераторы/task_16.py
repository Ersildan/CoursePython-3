class CardDeck:
    def __init__(self):
        suit = ('пик', 'треф', 'бубен', 'червей')
        number = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз')
        self.deck = iter(f'{j} {i}' for i in suit for j in number)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.deck)

cards = CardDeck()

print(next(cards))
print(next(cards))