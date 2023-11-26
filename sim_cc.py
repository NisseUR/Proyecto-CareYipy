# importar codigo de la codificacion de canal
import cc as cc

# Crear una instancia de la clase Codificacion_Canal
cod_canal = cc.Codificacion_Canal()

# Ejemplo de cómo utilizar las funciones
nombre_archivo_entrada = 'mensaje.bin'
nombre_archivo_salida = 'mensaje_codificado.bin'

# Leer el archivo binario utilizando el método de la instancia
datos_binarios = cod_canal.leer_archivo_binario(nombre_archivo_entrada)

# Convertir a cadena binaria utilizando el método de la instancia
cadena_binaria = cod_canal.bytes_a_cadena_binaria(datos_binarios)

# Eliminar espacios
cadena_binaria = cadena_binaria.replace(" ", "")  

# Aplicar codificación de canal utilizando el método de la instancia
datos_codificados = cod_canal.agregar_bit_paridad(cadena_binaria)

# Escribir datos codificados a un nuevo archivo utilizando el método de la instancia
cod_canal.escribir_archivo_binario(datos_codificados, nombre_archivo_salida)
