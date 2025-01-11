def matrix_by_elem(matrix):
    for row in matrix:
        yield from row


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(*matrix_by_elem(matrix)) # 1 2 3 4 5 6 7 8 9