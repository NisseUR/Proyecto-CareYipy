"""
Modulo: Desmodulador por aplitud de pulso (PAM)

Este modulo es el designado a combertir el mensaje del ASK, 
en bits.

"""

# Convierte decimal a binario.
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:].zfill(11)
    binary = ''.join('0' if bit == '0' else '1' for bit in binary)
    return binary

# Obtiene los bits con la amplitud brindad
def amp_to_bin(mapped_value, n, M):
    
    valor_float = float(mapped_value) # Convierte la amplitud en valor decimal
    
    diff = n/((2**M)-1) # Se calcula el valor de la amplitud.
    
    # Redondeo y obtencion de los grupos de bits.
    binary_value = round((valor_float + n)/(2*diff))
    binary = decimal_to_binary(binary_value)
    
    return binary

# Toma el resultado de la primer muestra para evitar repeticion de letras
def demod_signal(demod_array):
    
    demod_array_sampled = []
    for i in range(len(demod_array)):
        if (i-1) % 30 == 0: # Verifica que i sea multiplo de 30
            demod_array_sampled.append(demod_array[i-1])
    
    # Concatena todos los grupos de bits y lo convierte en string
    demod_bytes = ''.join(demod_array_sampled)
    demod_string = str(demod_bytes)
    
    # Guarda cadena de bits en un archivo 'demodulada_pam.bin'
    with open('demodulada_pam.bin', 'w') as file:
        file.write(demod_string)
        
    return demod_string

# Parametros del la señal
M = 11 # Cantidad de bits por simbolo
n = 5 # Amplitud maxima de la señal modulada

with open('senal_con_ruido.bin', 'r') as file:
    data = file.read().strip()  # Lee los datos.
    señal = data.split(",")
        
# Realiza la demodulacion para cada valor de amplitud muestreado

binary_values = []
for i in range(len(señal)):
    x = amp_to_bin(señal[i], n, M)
    binary_values.append(x)
    

demod = demod_signal(binary_values)