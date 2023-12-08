
with open("mensaje_inicial.txt", "r") as archivo_txt, open("mensaje_inicial.bin", "w") as archivo_bin:
    dentro_mensaje = archivo_txt.read() # Leer contenido del archivo de texto

    bkT = [] # array
    bfT = '' 
    
    for k in dentro_mensaje: 
        vT = k 
        bkT.append(format(ord(vT), '07b')) 
    for i in bkT:
        bfT = bfT + ''.join(i)
    archivo_bin.write(f"{bfT}\n")