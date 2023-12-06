def calcular_bit_paridad(byte):
    """Calcula el bit de paridad para un byte."""
    num_unos = sum([int(bit) for bit in byte])
    return '1' if num_unos % 2 != 0 else '0'

def codificar_con_paridad(input_file_path, output_file_path):
    """Codifica los datos de un archivo binario utilizando bits de paridad."""
    with open(input_file_path, 'rb') as file:
        contenido = file.read().decode('utf-8')

    bytes_codificados = []
    for byte in contenido.strip().split(' '):
        bit_paridad = calcular_bit_paridad(byte)
        bytes_codificados.append(byte + bit_paridad)

    datos_codificados = ''.join(bytes_codificados)  # Unir sin espacios

    # Escribir los datos codificados en un archivo binario
    with open(output_file_path, 'wb') as file:
        file.write(datos_codificados.encode('utf-8'))

    return output_file_path

# Ejemplo de uso
input_file = 'mensaje.bin'  
output_file = 'mensaje_codificado.bin' 

# Codificar el archivo
archivo_codificado = codificar_con_paridad(input_file, output_file)
print(f"Archivo codificado generado: {archivo_codificado}")
