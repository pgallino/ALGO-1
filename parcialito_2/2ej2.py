# Se tiene un archivo CSV de tres columnas llamado `operaciones.csv`. Las columnas son: 
#   - cuenta (cadena indicando el nombre de la cuenta) 
#   - operacion (tipo de la operación: `“extraccion”` o `“deposito”`)
#   - monto (valor de la operación, un entero positivo). 
# El archivo no tiene errores, está ordenado por el campo “Cuenta” y tiene encabezado con 
# el nombre de cada columna.

# Se pide escribir una funcion `calcular_balances` que genere un archivo `balances.csv` 
# con el balance de cada cuenta tras procesar las operaciones 
# presentes en el archivo `operaciones.csv`. 
# El archivo debe tener el formato y encabezado `cuenta,balance`. 

# Notas: 
# - Se debe asumir un balance inicial de 0. 
# - Las extracciones restan al valor del balance y los depósitos suman al mismo,  y si se desea 
# realizar una extraccion de mas plata que el monto disponible, la operacion no se realiza. 
# - Al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos 
# abiertos deben quedar cerrados.


# Escribir debajo de este comentario el código del ejercicio

import csv

def calcular_balances(ruta_archivo_original, ruta_archivo_destino):
    diccionario = {}
    with open(ruta_archivo_original) as original, open(ruta_archivo_destino, "w") as destino:
        
        lector = csv.DictReader(original)
        for fila in lector:
            cuenta = fila["cuenta"]
            operacion = fila["operacion"]
            monto = fila["monto"]
            if operacion == "deposito":
                diccionario[cuenta] = diccionario.get(cuenta, 0) + int(monto)
            elif operacion == "extraccion":
                if int(monto) > diccionario.get(cuenta, 0):
                    continue
                elif int(monto) <= diccionario.get(cuenta, 0):
                    diccionario[cuenta] = diccionario.get(cuenta, 0 ) - int(monto)
        
        destino.write(f"cuenta,balance\n")

        for clave in diccionario:                                           #considero que todos los balances y los nombres de las cuentas entran en la memoria RAM
            destino.write(f"{clave},{diccionario[clave]}\n")


            

            
# Pruebas

calcular_balances("operaciones.csv", "balances.csv")

with open('balances.csv') as f:
    lineas = f.read().splitlines()
    assert 'Cuenta de Nora,27' in lineas
