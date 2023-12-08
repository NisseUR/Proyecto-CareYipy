"""
Modulo: Modulacion por aplitud de pulso (PAM)

Este modulo es el designado a combertir las tramas de 11 bits generada por el codificador de canal, 
en una amplitud de pulso especifica, para ser modulada con ASK.

1. Se debe crear una matriz la cual agrupe por filas las tramas de datos.
2. Convertir las tramas de 11 datos binarios en un valor entre [-1 , 1]. 


"""

#Librerías utilizadas.
import matplotlib.pyplot as plt
import numpy as np

"""
La función defmuestreo recibe 1s y 0s y retarna un dato entre 5 y -5.
"""

def defmuestreo(trama_binaria):

    bin_string = ''.join(str(bit) for bit in trama_binaria) #Se convierte la lista en un str.

    bin_int = int(bin_string, 2) #Se convierte la lista de string en enteros.

    M = len(bin_string) # Cantidad de bits. (11)

    diff = 5/((2**M)-1) # Distancia entre rangos.

    mapeo = (2*bin_int*diff)-5 # Valor mapeado dentro del rango [n , -n]

    return mapeo

"""
Guarda los valores en un archivo.
"""

def guardar_pam(x_n, filename):
    flat = [item for sublist in x_n for item in sublist]  # Se aplana los datos
    with open(filename, 'w') as file:
        data_line = ','.join(map(str, flat))  # Convertir datos separas por comas
        file.write(data_line)

"""
Muestra los datos modulados.
"""

def plot_onda(onda):
    flat = [item for sublist in onda for item in sublist]  # Se aplana los datos

    # Crear un arreglo para el eje x
    x_axis = np.arange(len(flat))

    # Graficar los valores de `flat` en función del eje x
    plt.plot(x_axis, flat)
    plt.xlabel('Número de muestra n')
    plt.ylabel('x(n) = a_i*p(n)')
    plt.title('Representación discreta de una  señal PAM sin ruido')
    plt.grid(True)
    plt.show() 


archivo = 'msj_codificado.bin'  #Se debe cambiar este nombre.
with open(archivo, 'r') as file:
    datos = file.read().strip()  # Almacena en datos el contenido del archivo y se eliminan espacias en blanco.

    # Se crea una matriz, donde la secuencia se agrupa en filas de 11 bits.
    matriz_datos_binarios = [list(map(int, datos[i:i+11])) for i in range(0, len(datos), 11)]


#Muesreo de los datos
matriz_datos = []
for trama in matriz_datos_binarios:
    muestreo = defmuestreo(trama)
    matriz_datos.append(muestreo) 

#Repetir el dato 30 veces (Generar pulso)
t_pulso = ([1]*30)
 
onda_modulada = []
for i in matriz_datos:
    pulso = []
    for j in t_pulso:
        pulso.append(i*j)
    onda_modulada.append(pulso)

print(onda_modulada)


filename = 'mod_pam.bin'
guardar_pam(onda_modulada, filename)
plot_onda(onda_modulada)   

