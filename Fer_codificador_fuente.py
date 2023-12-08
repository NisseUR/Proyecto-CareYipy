
with open("mensaje_inicial.txt", "r") as archivo_txt, open("mensaje_inicial.bin", "w") as archivo_bin:
    dentro_mensaje = archivo_txt.read() # Leer contenido del archivo de texto

    bkT = [] # arreglo de codificador de fuente
    bfT = '' 
    
    for k in dentro_mensaje: # Caracter o pixel
        vT = k # Almacenamiento de muestra
        #if(vT != ' '):
        bkT.append(format(ord(vT), '07b')) # Secuencia de bits
       # else:
       #     bkT.append(vT)

    for i in bkT:
        bfT = bfT + ''.join(i) # Secuencia concatenada a la salida del codificador de fuente
    archivo_bin.write(f"{bfT}\n")