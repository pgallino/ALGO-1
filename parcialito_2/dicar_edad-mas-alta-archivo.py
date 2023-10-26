"""Escribir una función que reciba el nombre de un archivo, el cual en cada línea tiene un nombre y una edad, separados por una coma. 

Devolver en forma de tupla la edad más alta y una lista de nombres de todas las personas que tienen dicha edad.

Se puede abrir y recorrer el archivo sólo una vez y el mismo no entra en memoria.

Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben quedar cerrados."""


def buscar_nombres_de_mayores(nombre_archivo):

    diccionario = {}
    edad_mas_alta = 0

    with open(nombre_archivo) as archivo:
        for linea in archivo:
            linea = linea.rstrip("\n")
            fila = linea.split(",")

            if int(fila[1]) >= edad_mas_alta:
                edad_mas_alta = int(fila[1])
                diccionario[int(fila[1])] = diccionario.get(int(fila[1]), []) + [fila[0]]
                diccionario = {edad_mas_alta:diccionario[edad_mas_alta]}
                
        return(edad_mas_alta, diccionario[edad_mas_alta])