"""Ejercicio 159 recursion

Hacer una función recursiva que recibe una lista L y una función f,

y devuelve una nueva lista que contiene al principio todos los elementos de L para los que f devuelve True,

y al final el resto de los elementos. No es necesario mantener el orden relativo de los elementos en cada grupo.

Ejemplo: particionar([7,8,3,5,2], es_par) → [8,2,5,3,7]"""

def espar(n):
    return n%2 == 0

def _particionar(lista, lista1, lista2):

    if not lista:
        return lista2 + lista1
    
    elif espar(lista[0]):
        return _particionar(lista[1:], lista1, lista2 + [lista[0]])
    
    elif not espar(lista[0]):
        return _particionar(lista[1:], lista1 + [lista[0]], lista2)

def particionar(lista):
    lista1 = []
    lista2 = []
    return _particionar(lista, lista1, lista2)

print(particionar([7,8,3,5,2]))



    