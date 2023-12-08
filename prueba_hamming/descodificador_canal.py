import numpy as np
import hamming as hmg

def read_encoded_message_from_file(filename):
    """Lee un archivo codificado y lo convierte en una matriz de bits."""
    with open(filename + ".bin", "rb") as file:
        encoded_content = file.read()
    return np.fromiter(encoded_content.decode(), dtype=int).reshape(-1, 11)

def calculate_syndrome_matrix(encoded_matrix, parity_matrix):
    """Calcula la matriz de síndrome para la matriz codificada dada."""
    syndrome_list = [hmg.binary_dot_product(encoded_row, parity_matrix) for encoded_row in encoded_matrix]
    return np.array(syndrome_list, dtype=int)

def correct_errors(encoded_matrix, syndrome_matrix, parity_matrix):
    """Corrige los errores en la matriz codificada basada en la matriz de síndrome."""
    for row_index, syndrome in enumerate(syndrome_matrix):
        if not np.all(syndrome == 0):
            matching_rows = np.where((parity_matrix == syndrome).all(axis=1))[0]
            if len(matching_rows) == 0:
                continue
            error_index = matching_rows[0]
            encoded_matrix[row_index, error_index] ^= 1
    return encoded_matrix[:, 4:]

def save_decoded_message_to_file(filename, decoded_matrix):
    """Guarda la matriz decodificada en un archivo."""
    with open(filename, "w") as file:
        for row in decoded_matrix:
            file.write(''.join(map(str, row)))