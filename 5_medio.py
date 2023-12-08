import numpy as np

# Abrir mensaje del modulador
with open("mod_ask.bin", "r") as file:
    tx_data = file.read()

# Separar los datos y convertir a flotantes
Tx_a = tx_data.split(',')
Tx = np.array([float(num) for num in Tx_a])

def medio_ruidoso(Tx, SNR):
    # Se genera el ruido gaussiano, misma longitud que Tx
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

# Se simula el medio con ruido
Rx = medio_ruidoso(Tx, SNR_dB)

# Guardar la señal con ruido en un archivo
with open('senal_con_ruido.bin', 'w') as archivo:
    archivo.write(','.join([str(valor) for valor in Rx]))
