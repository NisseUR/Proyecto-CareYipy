# codificacion de canal

class Codificacion_Canal:
    # lectura del archivo .bin
    def leer_archivo_binario(self, nombre_archivo):
        with open(nombre_archivo, 'rb') as archivo:
            contenido = archivo.read()
            return contenido
        
    # conversión de los datos a cadenas de bits 
    def bytes_a_cadena_binaria(self, datos_bytes):
        return ''.join(format(byte, '08b') for byte in datos_bytes)

    # aplicar codificacion de canal a la cadena de bits, mediante codificacion de paridad

    def agregar_bit_paridad(self, data):
        paridad = data.count('1') % 2 == 0  # True si el número de 1s es par
        return data + ('0' if paridad else '1')


    # escribir datos codificados a un nuevo archivo 
    def escribir_archivo_binario(self, datos_codificados, nombre_archivo_salida):
        # Convertir la cadena de bits a bytes
        datos_en_bytes = int(datos_codificados, 2).to_bytes((len(datos_codificados) + 7) // 8, byteorder='big')
        
        with open(nombre_archivo_salida, 'wb') as archivo:
            archivo.write(datos_en_bytes)