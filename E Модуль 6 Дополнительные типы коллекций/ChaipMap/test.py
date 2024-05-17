with open('test.txt', 'a', encoding='utf-8') as file:
    file.write('\nYep,new text!')
with open('test.txt', encoding='utf-8') as f:
    print(f.read())
