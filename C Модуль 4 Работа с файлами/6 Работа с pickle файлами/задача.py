import pickle

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

dumped_matrix = pickle.dumps(matrix)
loaded_matrix = pickle.loads(dumped_matrix)

print(matrix == loaded_matrix)
print(matrix is loaded_matrix)