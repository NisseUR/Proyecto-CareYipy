"""

Se corre este archivo luego de la codificacion de fuente y antes de la modulacion

"""

import numpy as np
import hamming as hmg 
import codificador_canal as cc


def codificar_mensaje(source_file, channel_file, rows, cols):
    source_bits = cc.binary_file_to_number_list(source_file)
    P = np.array([[1, 0, 0, 1], [1, 1, 1, 0], [0, 1, 1, 1],
                  [1, 1, 0, 0], [1, 0, 1, 1], [1, 0, 1, 0], [1, 1, 1, 1]])
    I = hmg.create_identity_matrix(rows, rows)
    G = hmg.merge_matrices_horizontally(P, I)
    channel_bits = [hmg.binary_dot_product(block, G).tolist() for block in source_bits]
    cc.save_to_file(channel_file, channel_bits)

# Codificación del mensaje
codificar_mensaje("mensaje.bin", "msj_codificado.bin", 7, 4)
