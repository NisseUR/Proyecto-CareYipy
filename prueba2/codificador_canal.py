def calcular_bit_paridad(byte):
    """Calcula el bit de paridad para un byte."""
    # Contar cuántos '1' hay en el byte
    num_unos = sum([int(bit) for bit in byte])
    # Paridad par: si el número de '1's es impar, el bit de paridad es '1'
    return '1' if num_unos % 2 != 0 else '0'

def codificar_con_paridad(file_path):
    """Lee un archivo y codifica su contenido utilizando bits de paridad."""
    with open(file_path, 'rb') as file:
        # Leer el contenido del archivo como una cadena de texto
        contenido = file.read().decode('utf-8')

    # Dividir el contenido en bytes (separados por espacios) y procesar cada uno
    bytes_codificados = []
    for byte in contenido.strip().split(' '):
        bit_paridad = calcular_bit_paridad(byte)
        bytes_codificados.append(byte + bit_paridad)

    # Unir todos los bytes codificados en una sola cadena
    return ' '.join(bytes_codificados)

# Uso del código para codificar el archivo
file_path = '/home/nisse/UCR/comu/proyecto_final/Proyecto-CareYipy/prueba2/mensaje.bin'
datos_codificados = codificar_con_paridad(file_path)
print(datos_codificados) 
