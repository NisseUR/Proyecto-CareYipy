import codificador_canal as cc
import descodificador_canal as dc
import data_corruptor as data
import math
import hamming as hmg 
import numpy as np

#codificacion de canal

source_encoded_file = "mensaje.bin"
rows = 7  # Número de filas para la matriz Hamming
columns = 4  # Número de columnas para la matriz Hamming
channel_encoded_file = "mensaje_codif_canal.bin"
# Conversión del archivo binario a una lista de números
source_bits = cc.binary_file_to_number_list(source_encoded_file)

# Generación de la matriz de Hamming
P = np.array([[1, 0, 0, 1],
              [1, 1, 1, 0],
              [0, 1, 1, 1],
              [1, 1, 0, 0],
              [1, 0, 1, 1],
              [1, 0, 1, 0],
              [1, 1, 1, 1]])
I = hmg.create_identity_matrix(rows, rows)
G = hmg.merge_matrices_horizontally(P, I)

# Codificación de los bits de la fuente
channel_bits = []
for source_block in source_bits:
    encoded_block = hmg.binary_dot_product(source_block, G).tolist()
    channel_bits.append(encoded_block)

# Guardar el mensaje codificado
cc.save_to_file(channel_encoded_file, channel_bits)


#############################################################################
#data corruptor
error_rate = 0.07  # Tasa de error en el canal
input_file_name = "mensaje_codif_canal"
output_file_name = "codificado_BS.bin"
bits_in_block = 11


binary_content = data.read_binary_file(input_file_name)
bit_blocks = data.split_into_bit_blocks(binary_content, bits_in_block)
corrupted_data = data.introduce_errors(bit_blocks, error_rate)
data.save_to_file(output_file_name, corrupted_data)


print(f"Código con errores: v = {corrupted_data}")
print(f"\nPorcentaje de error: {error_rate * 100}%")
print(f"\nCantidad de bits erróneos: {math.ceil(bits_in_block * len(bit_blocks) * error_rate)}\n")

#############################################################################

# descodificador de canal

parity_matrix = np.array([[1, 0, 0, 1],
                          [1, 1, 1, 0],
                          [0, 1, 1, 1],
                          [1, 1, 0, 0],
                          [1, 0, 1, 1],
                          [1, 0, 1, 0],
                          [1, 1, 1, 1]])
rows, cols = parity_matrix.shape

# Generar la matriz H
H = hmg.merge_matrices_vertically(parity_matrix, hmg.create_identity_matrix(cols, cols))

# Leer y procesar el mensaje codificado
encoded_message = dc.read_encoded_message_from_file("codificado_BS")
syndrome_matrix = dc.calculate_syndrome_matrix(encoded_message, H)
decoded_message = dc.correct_errors(encoded_message, syndrome_matrix, H)

# Guardar y mostrar resultados
dc.save_decoded_message_to_file("mensaje_decodif_canal.bin", decoded_message)
print(f"Mensaje decodificado: {decoded_message.tolist()}")