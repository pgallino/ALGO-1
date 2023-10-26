"""Dado un diccionario cuyas claves son strings y sus valores son listas de enteros, escribir una función que invierta dicho diccionario de la siguiente forma:

cada valor de cada lista pasará a ser una clave del diccionario resultante, que tendrá como valor una lista de todas las claves en las que era un valor.

Por ejemplo, d = {"clave_1": [1,2,3], "clave_2": [4,6], "clave_3": [1,4]} 

dara como resultado {1: ["clave_1", "clave_3"], 2: ["clave_1"], 3: ["clave_1"], 4: ["clave_2", "clave_3"], 6: ["clave_2"]}"""

def dar_vuelta_diccionario(diccionario_origen):
    diccionario_invertido = {}
    for clave in diccionario_origen:
        for valor in diccionario_origen[clave]:
            diccionario_invertido[valor] = diccionario_invertido.get(valor, []) + [clave]
    return diccionario_invertido