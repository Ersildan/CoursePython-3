from re import search, IGNORECASE
for el in open(0):
    match = search('^Здравствуйте.?|^Доброе утро.?|^Добрый день.?|^Добрый вечер.?',
                      el.rstrip('\n'), flags=IGNORECASE)
    print(bool(match))