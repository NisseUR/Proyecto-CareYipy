class Codificacion_Canal:
    def leer_archivo_binario(self, nombre_archivo):
        with open(nombre_archivo, 'rb') as archivo:
            contenido = archivo.read()
        return ''.join(format(byte, '08b') for byte in contenido)

    def agregar_bit_paridad(self, data):
        datos_codificados = ""
        for i in range(0, len(data), 8):
            byte = data[i:i+8]
            paridad = '1' if byte.count('1') % 2 == 0 else '0'
            datos_codificados += byte + paridad
        return datos_codificados

    def escribir_archivo_binario(self, datos_codificados, nombre_archivo_salida):
        # Asegúrate de que la longitud de los datos codificados sea múltiplo de 8 para la conversión a bytes
        padding = '0' * ((8 - len(datos_codificados) % 8) % 8)
        datos_codificados_padded = datos_codificados + padding
        
        # Convertir cada 8 bits en un byte
        datos_en_bytes = bytearray()
        for i in range(0, len(datos_codificados_padded), 8):
            byte = datos_codificados_padded[i:i+8]
            datos_en_bytes.append(int(byte, 2))

        with open(nombre_archivo_salida, 'wb') as archivo:
            archivo.write(datos_en_bytes)