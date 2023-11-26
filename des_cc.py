class Decodificacion_Canal:
    def leer_archivo_binario(self, nombre_archivo):
        with open(nombre_archivo, 'rb') as archivo:
            contenido = archivo.read()
        return ''.join(format(byte, '08b') for byte in contenido)

    def verificar_y_eliminar_paridad(self, datos_codificados):
        datos_originales = ""
        for i in range(0, len(datos_codificados), 9):
            bloque = datos_codificados[i:i+9]
            paridad = bloque[-1]
            bloque_datos = bloque[:-1]
            if bloque_datos.count('1') % 2 == 0 and paridad == '0' or bloque_datos.count('1') % 2 != 0 and paridad == '1':
                datos_originales += bloque_datos
            else:
                print(f"Error de paridad detectado en el bloque: {bloque}")
        return datos_originales

    def binario_a_texto(self, datos_binarios):
        texto = ''
        for i in range(0, len(datos_binarios), 8):
            byte = datos_binarios[i:i+8]
            texto += chr(int(byte, 2))
        return texto