import numpy as np

def create_binary_matrix(n, m):
    return np.array([np.random.choice([0, 1], size=n, replace=True) for _ in range(m)]).T

def create_identity_matrix(n, m):
    return np.pad(np.eye(min(n, m), dtype=int), ((0, n - min(n, m)), (0, m - min(n, m))), 'constant', constant_values=(0))

def merge_matrices_horizontally(m_ti, matriz_identidad):
    return np.concatenate((m_ti, matriz_identidad), axis=1)

def merge_matrices_vertically(m1, m2):
    return np.concatenate((m2, m1), axis=0)

def binary_dot_product(vector, matrix):
    if len(vector) != matrix.shape[0]:
        raise ValueError("vector debe coincidir con numero de filas")
    return np.dot(vector, matrix) % 2