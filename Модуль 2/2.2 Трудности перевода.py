n = int(input())
languages = set(input().split(', '))

for i in range(n - 1):
    person_languages = set(input().split(', '))
    languages = languages.intersection(person_languages)

languages = sorted(languages)

if len(languages) > 0:
    print(*languages, sep=', ')
else:
    print('Сериал снять не удастся')
