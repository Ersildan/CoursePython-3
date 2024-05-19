from collections import ChainMap

animals = ChainMap({'monkey': 10, 'elephant': 3, 'lemur': 7},
                   {'monkey': 1, 'elephant': 2, 'lemur': 12, 'bear': 1})

print(animals.get('monkey'))
print(animals['bear'])