import math

# Demodulador 2048 PAM

# Parámetros globales
M = 11  # Cantidad de bits por símbolo
n = 5   # Amplitud máxima de la señal modulada
N = 30  # Tamaño de la lista de muestras
Tsim = 0.88e-3  # Periodo de la señal en segundos

def leer_y_procesar_archivo(ruta_archivo):
    """
    Lee un archivo y convierte su contenido en una lista de valores flotantes.

    :param ruta_archivo: Ruta del archivo a leer.
    :return: Lista de valores flotantes leídos del archivo.
    """
    with open(ruta_archivo, 'r') as archivo:
        valores = [float(valor) for valor in archivo.read().strip().split(',')]
    return valores

def generar_cos_demodular_ask(valores, N, Tsim):
    """
    Genera una señal coseno y realiza la demodulación ASK de los valores proporcionados.

    :param valores: Lista de valores de la señal modulada.
    :param N: Número de muestras.
    :param Tsim: Periodo de la señal.
    :return: Lista de valores demodulados.
    """
    Ts = Tsim / N
    t = 0
    c_k = [math.cos(2 * math.pi * t / Tsim) for _ in range(N)]
    t += Ts

    valores_demodulados = [valor / c_k[i % N] for i, valor in enumerate(valores)]
    return valores_demodulados

def obtener_simbolos_binarios(valores, n, M):
    """
    Convierte los valores demodulados en símbolos binarios.

    :param valores: Lista de valores demodulados.
    :param n: Amplitud máxima de la señal.
    :param M: Cantidad de bits por símbolo.
    :return: Lista de símbolos binarios.
    """
    a_n = n / ((2 ** M) - 1)
    simbolos_binarios = [bin(round((valor + n) / (2 * a_n)))[2:].zfill(M) for valor in valores]
    return simbolos_binarios

def procesar_demodulacion(simbolos):
    """
    Procesa los símbolos binarios para obtener la cadena final de datos demodulados.

    :param simbolos: Lista de símbolos binarios.
    :return: Cadena de caracteres que representa los datos demodulados.
    """
    return ''.join(simbolos[i] for i in range(len(simbolos)) if (i - 1) % (N * N) == 0)

def demodulacion_total(ruta_archivo):
    """
    Realiza el proceso completo de demodulación.

    :param ruta_archivo: Ruta del archivo con la señal modulada.
    :return: Cadena de caracteres con los datos demodulados.
    """
    valores = leer_y_procesar_archivo(ruta_archivo)
    valores_demodulados = generar_cos_demodular_ask(valores, N, Tsim)
    simbolos_binarios = obtener_simbolos_binarios(valores_demodulados, n, M)
    cadena_demodulada = procesar_demodulacion(simbolos_binarios)

    with open('demodulada_ask.bin', 'w') as archivo:
        archivo.write(cadena_demodulada)

    return cadena_demodulada

# Ejecución del proceso de demodulación
resultado_demodulacion = demodulacion_total('mod_ask.bin')
