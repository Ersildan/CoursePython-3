class Alphabet:
    def __init__(self, language):

        self.language = language
        self.letter_en = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
        self.letter_ru = ('а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м',
                          'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ',
                          'ъ', 'ы', 'ь', 'э', 'ю', 'я')

        if self.language == 'en':
            self.data = iter(_ for _ in self.letter_en)
        else:
            self.data = iter(_ for _ in self.letter_ru)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.data)
        except:
            if self.language == 'en':
                self.data = iter(_ for _ in self.letter_en)
                return next(self.data)
            else:
                self.data = iter(_ for _ in self.letter_ru)
                return next(self.data)

en_alpha = Alphabet('en')

letters = [next(en_alpha) for _ in range(28)]

print(*letters)
