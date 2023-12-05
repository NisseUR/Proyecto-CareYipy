mensaje = "Hola Mundo"
binario = ' '.join(format(ord(c), '08b') for c in mensaje)

# Convertir la cadena de bits a bytes para escribir en un archivo binario
datos_binarios = bytes(binario, 'utf-8')

# Escribir en el archivo mensaje.bin
with open('mensaje.bin', 'wb') as archivo:
    archivo.write(datos_binarios)
