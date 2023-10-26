"""Escribir una función que reciba una cadena y devuelva un diccionario cuyas claves sean las letras y cuyos valores sean la cantidad de apariciones de dicha letra.
Por ejemplo, si recibe 'catamarca' debe devolver: {'c':2, 'a':4, 't':1, 'r':1, 'm':1}"""

def contador_letras(cadena):
    recuento = {}
    for caracter in cadena.lower().replace(" ",""):
        recuento[caracter] = recuento.get(caracter, 0) + 1
    return recuento