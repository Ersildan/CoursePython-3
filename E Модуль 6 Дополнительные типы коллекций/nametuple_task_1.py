from collections import namedtuple
import pickle

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open('data.pkl', 'rb') as file:
    lst = pickle.load(file)
    for i in lst:
        for field, value in zip(Animal._fields, i):
            print(field, ':', value)
        print()
