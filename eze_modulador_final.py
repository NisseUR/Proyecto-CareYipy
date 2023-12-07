# -*- coding: utf-8 -*-
"""
Creado el Tue Dec 5 18:44:09 2023

@author: Ezequiel
"""

import math
import matplotlib.pyplot as plt
import numpy as np

def procesar_archivo_pam(ruta_archivo):
    """
    Lee un archivo PAM y lo convierte en una lista de valores flotantes.

    :param ruta_archivo: Ruta del archivo PAM a procesar.
    :return: Lista de valores flotantes leídos del archivo.
    """
    with open(ruta_archivo, 'r') as archivo:
        datos = [float(valor) for valor in archivo.read().strip().split(',')]
    return datos

def generar_senal_cos_y_modular_ask(valores_pam, num_muestras, duracion_sim):
    """
    Genera una señal coseno y realiza la modulación ASK con los valores PAM.

    :param valores_pam: Lista de valores PAM a modular.
    :param num_muestras: Número de muestras para la señal coseno.
    :param duracion_sim: Duración de la simulación.
    :return: Lista de valores de la señal ASK modulada.
    """
    intervalo_muestreo, tiempo_actual = duracion_sim / num_muestras, 0
    senal_modulada = []

    for _ in range(num_muestras):
        cos_muestra = math.cos(2 * math.pi * tiempo_actual / duracion_sim)
        tiempo_actual += intervalo_muestreo
        senal_modulada.extend([valor * cos_muestra for valor in valores_pam])

    return senal_modulada

def guardar_y_graficar_ask(senal_modulada, ruta_guardado):
    """
    Guarda la señal ASK modulada en un archivo y la grafica.

    :param senal_modulada: Lista de valores de la señal ASK modulada.
    :param ruta_guardado: Ruta del archivo para guardar la señal modulada.
    """
    with open(ruta_guardado, 'w') as archivo:
        archivo.write(','.join(map(str, senal_modulada)))

    plt.plot(np.arange(len(senal_modulada)), senal_modulada)
    plt.xlabel('Muestra n')
    plt.ylabel('s(n)')
    plt.title('Gráfico de señal ASK')
    plt.grid(True)
    plt.show()

# Ejecución del proceso de modulación
ruta_pam = 'mod_pam.bin'
valores_pam = procesar_archivo_pam(ruta_pam)

num_muestras = 1
duracion_simulacion = 0.88e-3

senal_ask = generar_senal_cos_y_modular_ask(valores_pam, num_muestras, duracion_simulacion)

ruta_ask = 'mod_ask.bin'
guardar_y_graficar_ask(senal_ask, ruta_ask)
