"""Se tiene un diccionario donde cada clave es el título de una canción (cadena), y cada valor la duración de la canción (en segundos).

Se tiene asimismo otro diccionario donde cada clave es el título de una lista de reproducción (cadena), y cada valor una lista con títulos de canción que la componen.

Se pide implementar una función que reciba como parámetros ambos diccionarios, y devuelva en forma de diccionario las duraciones de cada lista de reproducción. 

(El diccionario devuelto debe tener como claves los títulos de lista, y como valor la duración en segundos.)"""

def duracion_lista(diccionario_lista, diccionario_canciones):
    lista_duraciones = {}
    for clave in diccionario_lista:
        duracion = 0
        for cancion in diccionario_canciones:
            if cancion in diccionario_lista[clave]:
                duracion += diccionario_canciones[cancion]
                lista_duraciones[clave] = duracion
    return lista_duraciones


#def obtener_duracion_listas(canciones, listas_reproduccion):
#    resultado={}
#    for clave in listas_reproduccion:
#        duracion = 0
#        for cancion in listas_reproduccion[clave]:
#            duracion += canciones[cancion]
#        resultado[clave] = duracion
#    return resultado