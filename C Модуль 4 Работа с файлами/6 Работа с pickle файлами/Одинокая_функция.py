import pickle
import sys

with open(input(), 'rb') as file:
    alone_function = pickle.load(file)
    data = list(map(str.strip, sys.stdin))
    print(alone_function(*data))
