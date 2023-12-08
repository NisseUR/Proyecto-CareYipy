# Abrir el archivo de texto para lectura y el archivo binario para escritura
with open("mensaje_inicial.txt", "r") as archivo_txt, open("mensaje_inicial.bin", "w") as archivo_bin:

    dentro_mensaje = archivo_txt.read()


    bfT = ''.join(format(ord(char), '07b') for char in dentro_mensaje)

    # Escribir la cadena binaria en el archivo binario
    archivo_bin.write(f"{bfT}\n")