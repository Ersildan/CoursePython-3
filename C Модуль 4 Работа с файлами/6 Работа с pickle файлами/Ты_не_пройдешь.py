import pickle


def filter_dump(filename, objects, typename):
    with open(filename, 'wb') as file:
        lst = [i for i in objects if type(i) == typename]
        pickle.dump(lst, file)
    return file


print(filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int))
