# Leer el contenido del archivo mensaje.bin y mostrarlo
with open('mensaje_codificado.bin', 'rb') as archivo:
    contenido_mensaje_bin = archivo.read()

print(contenido_mensaje_bin)
