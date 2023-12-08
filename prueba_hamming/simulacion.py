import numpy as np
import math
import hamming as hmg 
import codificador_canal as cc
import descodificador_canal as dc
import data_corruptor as data

def codificar_mensaje(source_file, channel_file, rows, cols):
    source_bits = cc.binary_file_to_number_list(source_file)
    P = np.array([[1, 0, 0, 1], [1, 1, 1, 0], [0, 1, 1, 1],
                  [1, 1, 0, 0], [1, 0, 1, 1], [1, 0, 1, 0], [1, 1, 1, 1]])
    I = hmg.create_identity_matrix(rows, rows)
    G = hmg.merge_matrices_horizontally(P, I)
    channel_bits = [hmg.binary_dot_product(block, G).tolist() for block in source_bits]
    cc.save_to_file(channel_file, channel_bits)

def corromper_datos(input_file, output_file, error_rate, bits_per_block):
    binary_content = data.read_binary_file(input_file)
    bit_blocks = data.split_into_bit_blocks(binary_content, bits_per_block)
    corrupted_data = data.introduce_errors(bit_blocks, error_rate)
    data.save_to_file(output_file, corrupted_data)
    return corrupted_data

def decodificar_mensaje(encoded_file, decoded_file):
    parity_matrix = np.array([[1, 0, 0, 1], [1, 1, 1, 0], [0, 1, 1, 1],
                              [1, 1, 0, 0], [1, 0, 1, 1], [1, 0, 1, 0], [1, 1, 1, 1]])
    cols = parity_matrix.shape[1]
    H = hmg.merge_matrices_vertically(parity_matrix, hmg.create_identity_matrix(cols, cols))
    encoded_message = dc.read_encoded_message_from_file(encoded_file)
    syndrome_matrix = dc.calculate_syndrome_matrix(encoded_message, H)
    decoded_message = dc.correct_errors(encoded_message, syndrome_matrix, H)
    dc.save_decoded_message_to_file(decoded_file, decoded_message)
    return decoded_message

# Codificación del mensaje
codificar_mensaje("mensaje.bin", "msj_codificado.bin", 7, 4)

# Corrupción de datos
corrupted_data = corromper_datos("msj_codificado", "msj_codificado_corrupcion.bin", 0.07, 11)
print(f"Código con implementación de errores: v = {corrupted_data}")
print(f"\nPorcentaje de error: {0.07 * 100}%")
print(f"\nCantidad de bits erróneos: {math.ceil(11 * len(corrupted_data) * 0.07)}\n")

# Decodificación del mensaje
decoded_message = decodificar_mensaje("msj_codificado_corrupcion", "msj_decodificado.bin")
print(f"El mensaje decodificado corresponde a: {decoded_message.tolist()}")