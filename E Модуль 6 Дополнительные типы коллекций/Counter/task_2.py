from collections import Counter


def count_occurences(word, words):
    return Counter(words.lower().split())[word.lower()]


word = 'Se'
words = 'se sdsf sds SE sdfsdg Se dhgf gfd asd se'

print(count_occurences(word, words))
