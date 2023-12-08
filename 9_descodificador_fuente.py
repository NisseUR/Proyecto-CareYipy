def decodificar_mensaje(nombre_archivo):
    import re

    with open(nombre_archivo + ".bin", "r") as archivo_bin, open("mensaje_final.txt", "w") as archivo_txt:
        contenido_binario = archivo_bin.readlines()

        binario_concatenado = ''.join(linea for linea in contenido_binario)
        palabras_binarias = binario_concatenado.split()

        lista_caracteres_ascii = []

        for palabra_binaria in palabras_binarias:
            grupos_binarios = re.findall('.{1,7}', palabra_binaria)
            for grupo in grupos_binarios:
                valor_decimal = int(grupo, 2)
                caracter_ascii = chr(valor_decimal)
                lista_caracteres_ascii.append(caracter_ascii)
            lista_caracteres_ascii.append(' ')
        lista_caracteres_ascii.pop()

        archivo_txt.write(''.join(lista_caracteres_ascii))

        return lista_caracteres_ascii

mensaje_decodificado = decodificar_mensaje("msj_decodificado")
