import numpy as np

with open("mod_ask.bin", "r") as file:
    tx_data = file.read()

# Separar los datos y convertir a flotantes
Tx_a = tx_data.split(',')
Tx = np.array([float(num) for num in Tx_a])

def medio(Tx, SNR):

    ruido = np.random.randn(len(Tx))


    pot_xT = np.mean(np.abs(Tx) ** 2)


    pot_ruido = pot_xT / (10 ** (SNR / 10))

    ruido *= np.sqrt(pot_ruido)

    xR = Tx + ruido

    return xR

SNR_dB = 90

Rx = medio(Tx, SNR_dB)

# Guardar la señal con ruido en un archivo
with open('senal_con_ruido.bin', 'w') as archivo:
    archivo.write(','.join([str(valor) for valor in Rx]))