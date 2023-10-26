"""Escribir una función que reciba por parámetro una cadena 

y devuelva un diccionario cuyas claves sean las primeras letras de cada palabra y cuyo valor asociado sea una lista de palabras que empiezan con cada letra.

Por ejemplo, si recibe: 'Este es el parcial de algoritmos'. Debe devolver: {'d':['de'], 'a':['algoritmos'], 'e':['Este','es','el'],'p':['parcial']}"""

def contador_palabras_por_letra(cadena):
    diccionario = {}
    for palabra in cadena.lower().split():
        diccionario[palabra[0]] = diccionario.get(palabra[0], []) + [palabra]
    return diccionario