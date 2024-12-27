def transpose(matrix):
    return [list(item) for item in zip(*matrix)]

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for row in transpose(matrix):
    print(row)

''' [1, 4, 7]
    [2, 5, 8]
    [2, 5, 8]
'''