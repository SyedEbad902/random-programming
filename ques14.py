import numpy as np

def multiply_matrices(A, B):
    result = np.dot(A, B)
    return result

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
matrix_result = multiply_matrices(A, B)
matrix_result
