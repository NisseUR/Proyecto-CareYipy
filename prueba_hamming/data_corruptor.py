import numpy as np
import math

def read_binary_file(file_name):
    """Lee un archivo binario y devuelve su contenido."""
    with open(file_name + ".bin", "rb") as file:
        data = file.read()
    return data.decode()

def split_into_bit_blocks(binary_data, block_size):
    """Divide una cadena binaria en bloques de tamaño especificado."""
    return [list(binary_data[i:i + block_size]) for i in range(0, len(binary_data), block_size)]

def introduce_errors(bit_blocks, error_percentage):
    """Introduce errores en los bloques de bits según el porcentaje de error."""
    corrupted_blocks = []
    for block in bit_blocks:
        num_errors = int(math.ceil(len(block) * error_percentage))
        error_positions = np.random.choice(len(block), num_errors, replace=False)
        for pos in error_positions:
            block[pos] = '1' if block[pos] == '0' else '0'
        corrupted_blocks.append(block)
    return corrupted_blocks

def save_to_file(file_name, bit_blocks):
    """Guarda bloques de bits en un archivo."""
    with open(file_name, "w") as file:
        for block in bit_blocks:
            file.write("".join(block))
