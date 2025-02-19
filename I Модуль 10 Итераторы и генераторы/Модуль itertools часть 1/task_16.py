from itertools import cycle, zip_longest

def roundrobin(*args):
    return (char for obj in zip_longest(*args, fillvalue= '') for char in obj if char != '')

print(*roundrobin('abc', 'd', 'ef'))

