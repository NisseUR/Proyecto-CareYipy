"""
Modulo: Canal de tranmisión.

"""
import numpy as np
from decimal import Decimal

# Abrir mensaje del modulador 
with open("mod_ask.bin", "r") as file: 
    tx_data = file.read() 
    

#manipulacion de los datos para poder procesar.
tx_data = tx_data.decode('utf-8')
tx_data = tx_data.split(',')

Tx_a = []
for num in tx_data:
    formato_num = "{:.16f}".format(float(num))
    Tx_a.append(formato_num)

decimal_array = np.array([Decimal(num) for num in Tx_a])

#Tx son los datos a meterle reuido.
Tx = np.array(decimal_array, dtype=float)

def medio_ruidoso(Tx, SNR):
    # Se genera el ruido gaussiano, misma longitud que xT
    ruido = np.random.randn(len(Tx))

    # Se calcula la potencia de la señal que se transmite
    pot_xT = np.mean(np.abs(Tx) ** 2)

    # Se calcula la potencia del ruido en función de SNR
    pot_ruido = pot_xT / (10 ** (SNR / 10))

    # Se escala el ruido para que tenga la potencia deseada
    ruido *= np.sqrt(pot_ruido)

    # Se suma el ruido a la señal transmitida y se obtiene la señal recibida
    xR = Tx + ruido

    return xR

# Se define la relación señal-ruido (SNR) deseada en dB
SNR_dB = 90

# Se simula el medio con ruidoso
Rx = medio_ruidoso(Tx, SNR_dB)

with open('senal_con_ruido.bin', 'w') as archivo:
    archivo.write(','.join([str(valor) for valor in Rx]))