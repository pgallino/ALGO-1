"""Escribir una función que reciba una cadena (formada únicamente por letras y espacios),
y devuelva un diccionario donde para cada palabra muestre la cantidad de veces que es precedida por otra palabra. 

Ejemplo: “a la a hola es a es la hora a hola” → {“a”: {“hora”: 1, “es”: 1, “la”: 1}, “hola”: {“a”: 2}, ... }"""

def contar_precedidas(cadena):

    diccionario = {}
    palabras = cadena.lower().split()
    
    for indice in range(1,len(palabras)):
        palabra = palabras[indice]
        palabra_anterior = palabras[indice-1]
        diccionario[palabra] = diccionario.get(palabra, {})
        diccionario[palabra][palabra_anterior] = diccionario[palabra].get(palabra_anterior, 0) + 1

    return diccionario
