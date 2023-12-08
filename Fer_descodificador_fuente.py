def descodificacion(filename):
    
    import re

    with open(filename + ".bin", "r") as archivo_bin, open("descodificacion_mensaje.txt", "w") as archivo_txt:
        # Leer contenido del archivo binario
        bin_dentro = archivo_bin.readlines()

        # Convertir cada cadena de unos y ceros en un caracter ASCII y escribir en archivo de texto
        bfR = ''.join(c for c in bin_dentro) # Información recibida
        bkR = [] 

        bkR_w = bfR.split()

        lista_ascii = []

        for bkR in bkR_w:
            agrupaciones = re.findall('.{1,7}', bkR)
            for grupo in agrupaciones:
                decimales = int(grupo, 2)
                asciizz = chr(decimales)
                lista_ascii.append(asciizz)
            lista_ascii.append(' ')
        lista_ascii.pop() # ultimo caracter innecesario-

        archivo_txt.write(''.join(lista_ascii)) # Guardar mensaje decodificado en un archivo
        
        return lista_ascii
        
descodificado = descodificacion("decodif_canal_fin")