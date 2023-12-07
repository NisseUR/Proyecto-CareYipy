def calcular_bits_paridad(byte, num_bits_paridad=4):
    """Calcula varios bits de paridad para un byte."""
    bits_paridad = []
    for i in range(num_bits_paridad):
        num_unos = sum([int(bit) for bit in byte[i::num_bits_paridad]])
        bits_paridad.append('1' if num_unos % 2 != 0 else '0')
    return ''.join(bits_paridad)

def codificar_con_paridad(input_file_path, output_file_path, num_bits_paridad=4):
    """Codifica los datos de un archivo binario utilizando varios bits de paridad."""
    with open(input_file_path, 'r') as archivo_txt:
        contenido_txt = archivo_txt.read()  # Leer contenido del archivo de texto

    bkT = []  # arreglo de codificador de fuente
    for k in contenido_txt:  # Caracter o pixel
        bkT.append(format(ord(k), '07b'))  # Secuencia de bits

    bfT = ''.join(bkT)  # Secuencia concatenada a la salida del codificador de fuente

    bytes_codificados = []
    for i in range(0, len(bfT), 7):  # Procesar cada 7 bits (un byte en formato ASCII)
        byte = bfT[i:i+7]
        bits_paridad = calcular_bits_paridad(byte, num_bits_paridad)
        bytes_codificados.append(byte + bits_paridad)

    datos_codificados = ''.join(bytes_codificados)  # Sin espacios para bloques de 11 bits

    # Escribir los datos codificados en un archivo binario
    with open(output_file_path, 'w') as archivo_bin:
        archivo_bin.write(datos_codificados)

    # Calcular la razón de código
    razon_codigo = 7 / 11

    return output_file_path, razon_codigo

# Ejemplo de uso
input_file = 'mensaje.txt'  # Archivo de texto de entrada
output_file = 'mensaje_codificado.bin'  # Archivo binario de salida

# Codificar el archivo y obtener la razón de código
archivo_codificado, razon_codigo = codificar_con_paridad(input_file, output_file)
print(f"Archivo codificado generado: {archivo_codificado}")
print(f"Razón de código: {razon_codigo}")
