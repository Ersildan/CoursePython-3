def spell(*words):
    
    d = dict()
    words = [i.lower() for i in words]

    for word in words:
        l = word[0]
        d.update(d.fromkeys(l, max([len(word) for word in words if l in word and word[0] == l])))

    return d
    
'''Реализуйте функцию spell(), которая принимает произвольное количество
позиционных аргументов-слов и возвращает словарь, ключи которого — первые
буквы слов, а значения — максимальные длины слов на эту букву.
'''
