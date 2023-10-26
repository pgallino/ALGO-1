"""Escribir una función que reciba una cadena y devuelva una tupla con la palabra que tuvo mayor cantidad de apariciones, y la cantidad de apariciones que tuvo. 

Si hay dos o más palabras con máxima cantidad de apariciones, devolver cualquiera de ellas. 

La cadena contiene únicamente palabras y espacios. 

Ejemplo: "la cama la silla y la mesa" → ("la", 3)"""

def identificar_palabra_más_frecuente(cadena):
    cantidad_de_apariciones = {}
    for palabra in cadena.lower().split():
        cantidad_de_apariciones[palabra] = cantidad_de_apariciones.get(palabra, 0) + 1          #cuenta todas las palabras
    cantidad_de_apariciones_maxima = 0                                                      
    for clave in cantidad_de_apariciones:
        if cantidad_de_apariciones[clave] > cantidad_de_apariciones_maxima:                     #mira si la cantidad de apariciones de cada palabra es máxima
            cantidad_de_apariciones_maxima = cantidad_de_apariciones[clave]
            tupla = (clave, cantidad_de_apariciones_maxima)                                     #crea la tupla con la palabra y su cantidad de apariciones
    return tupla
        