# sim_des_cc.py
import des_cc as dcc

# Crear una instancia de la clase Decodificacion_Canal
decodificador = dcc.Decodificacion_Canal()

# Leer el archivo codificado
datos_codificados = decodificador.leer_archivo_binario('mensaje_codificado.bin')

# Verificar y eliminar la paridad
#datos_sin_paridad = decodificador.verificar_y_eliminar_paridad(datos_codificados)

# Convertir a texto
texto_original = decodificador.binario_a_texto(datos_sin_paridad)

print(texto_original)
