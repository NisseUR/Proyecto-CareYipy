def descodificar_con_paridad_y_calcular_error(input_file_path, mensaje_original, output_file_path, num_bits_paridad=4):
    """Descodifica los datos de un archivo binario y calcula el porcentaje de error."""
    with open(input_file_path, 'r') as archivo_bin:
        datos_codificados = archivo_bin.read()  # Leer contenido del archivo binario

    # Dividir los datos codificados en bloques de 11 bits (7 de datos + 4 de paridad)
    bloques_codificados = [datos_codificados[i:i+11] for i in range(0, len(datos_codificados), 11)]

    # Extraer los 7 bits de datos de cada bloque
    bloques_datos = [bloque[:7] for bloque in bloques_codificados]

    # Convertir cada bloque de datos a su carácter ASCII correspondiente
    caracteres_decodificados = [chr(int(bloque, 2)) for bloque in bloques_datos]

    # Unir todos los caracteres para formar el mensaje descodificado
    mensaje_descodificado = ''.join(caracteres_decodificados)

    # Escribir el mensaje descodificado en un archivo de texto
    with open(output_file_path, 'w') as archivo_txt:
        archivo_txt.write(mensaje_descodificado)

    # Calcular el porcentaje de error
    longitud_minima = min(len(mensaje_original), len(mensaje_descodificado))
    errores = sum(1 for i in range(longitud_minima) if mensaje_original[i] != mensaje_descodificado[i])
    porcentaje_error = (errores / longitud_minima) * 100

    return output_file_path, porcentaje_error

# Leer el contenido del mensaje original
with open('mensaje.txt', 'r') as file:
    contenido_mensaje_original = file.read()

# Ejemplo de uso
input_file = 'mensaje_codificado.bin'
output_file = 'mensaje_descodificado.txt'

# Descodificar el archivo y calcular el porcentaje de error
archivo_descodificado, porcentaje_error = descodificar_con_paridad_y_calcular_error(input_file, contenido_mensaje_original, output_file)
print(f"Archivo descodificado generado: {archivo_descodificado}")
print(f"Porcentaje de error: {porcentaje_error}%")
