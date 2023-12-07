import numpy as np

def create_binary_matrix(n, m):
    return np.array([np.random.choice([0, 1], size=n, replace=True) for _ in range(m)]).T

def create_identity_matrix(n, m):
    return np.pad(np.eye(min(n, m), dtype=int), ((0, n - min(n, m)), (0, m - min(n, m))), 'constant', constant_values=(0))

def merge_matrices_horizontally(lti_matrix, id_matrix):
    return np.concatenate((lti_matrix, id_matrix), axis=1)

def merge_matrices_vertically(matrix1, matrix2):
    return np.concatenate((matrix2, matrix1), axis=0)

def binary_dot_product(vector, matrix):
    if len(vector) != matrix.shape[0]:
        raise ValueError("longitud del vector debe coincidir con la cantidad de filas")
    return np.dot(vector, matrix) % 2