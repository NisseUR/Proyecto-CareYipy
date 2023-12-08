"""
Modulo: Desmodulador por aplitud de pulso (PAM)

Este modulo es el designado a combertir el mensaje del ASK, 
en bits.

"""

# Convierte decimal a binario
def conversion_a_binario(decimal):
    return format(decimal, '011b')

# Obtiene los bits con la amplitud brindada
def amp_to_bin(mapped_value, n, M):
    valor_float = float(mapped_value)  # Convierte la amplitud en valor decimal
    diff = n / ((2 ** M) - 1)  # Se calcula el valor de la amplitud
    
    # Redondeo y obtención de los grupos de bits
    binary_value = round((valor_float + n) / (2 * diff))
    return conversion_a_binario(binary_value)

# Toma el resultado de la primer muestra para evitar repetición de letras
def demod_signal(demod_array):
    # Muestreo de la señal demodulada
    demod_array_sampled = [demod_array[i] for i in range(len(demod_array)) if (i - 1) % 30 == 0]
    
    # Concatena todos los grupos de bits y los guarda en un archivo
    demod_string = ''.join(demod_array_sampled)
    with open('demodulada_pam.bin', 'w') as file:
        file.write(demod_string)
    
    return demod_string

# Parámetros de la señal
M = 11  # Cantidad de bits por símbolo
n = 5   # Amplitud máxima de la señal modulada

# Leer y procesar la señal
with open('senal_con_ruido.bin', 'r') as file:
    señal = file.read().strip().split(",")

# Realizar la demodulación para cada valor de amplitud muestreado
binary_values = [amp_to_bin(valor, n, M) for valor in señal]

# Obtener la señal demodulada
demod = demod_signal(binary_values)