from collections import Counter


def scrabble(symbols, word):
    return Counter(symbols.lower()) >= Counter(word.lower())


print(scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'))
