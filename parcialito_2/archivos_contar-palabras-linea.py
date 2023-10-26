"""Escribir una función que dado el nombre de un archivo devuelva un diccionario donde la clave es el número de línea 

y su valor asociado la cantidad de palabras que tiene esa línea. 

Asumir que cada línea contiene palabras separadas únicamente por espacios.

Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben quedar cerrados."""

def contar_palabras_linea(ruta_archivo):
    diccionario = {}
    numero_linea = 0

    with open(ruta_archivo) as archivo:

        for linea in archivo:
            numero_linea += 1
            clave = f"Línea {numero_linea}"
            palabras = set(linea.rstrip().lower().split())
            diccionario[clave] = len(palabras)
        
    return diccionario
