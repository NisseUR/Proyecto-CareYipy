import cc as cc

cod_canal = cc.Codificacion_Canal()
nombre_archivo_entrada = 'mensaje.bin'
nombre_archivo_salida = 'mensaje_codificado.bin'

datos_binarios = cod_canal.leer_archivo_binario(nombre_archivo_entrada)
cadena_binaria = datos_binarios.replace(" ", "")  # Eliminar espacios
datos_codificados = cod_canal.agregar_bit_paridad(cadena_binaria)
cod_canal.escribir_archivo_binario(datos_codificados, nombre_archivo_salida)
