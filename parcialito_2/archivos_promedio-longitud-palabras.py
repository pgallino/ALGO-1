"""Escribir una función que reciba la ruta a un archivo de texto, y devuelva el promedio del largo de las palabras de dicho texto
(considerando signos de puntuación y otros símbolos como parte de la palabra).

Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben quedar cerrados."""

def calcular_promedio_largo_palabra(ruta_archivo):

    with open(ruta_archivo, encoding = "utf-8") as archivo:
        promedio = 0
        cantidad_lineas = 0

        for linea in archivo:
            longitud_total = 0
            linea = linea.rstrip("\n").split()
            longitudes = list(map(len,linea))

            for indice in range(len(longitudes)):
                longitud_total += longitudes[indice]
                
            promedio += longitud_total/len(longitudes)
            cantidad_lineas += 1

        return promedio/cantidad_lineas