"""Ejercicio 134 pilas

Implementar una función que, dada una pila de números, devuelva otra pila que contenga únicamente los números pares de ésta

(manteniendo el orden relativo de los elementos según como estaban en la original).

La pila original debe preservar su estado original al salir de la función.

Es decir, debe conservar todos los elementos que tenía y el orden de los mismos antes de que la función fuese invocada."""

from Pila import Pila
from Pila import _Nodo

def apilar_pares(pila):
    pila_aux = Pila()
    pila_pares = Pila()
    pila_resultado = Pila()

    while not pila.esta_vacia():
        if pila.ver_tope() % 2 == 0:
            pila_pares.apilar(pila.ver_tope())
            pila_aux.apilar(pila.desapilar())
        else:
            pila_aux.apilar(pila.desapilar())

    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())
    
    while not pila_pares.esta_vacia():
        pila_resultado.apilar(pila_pares.desapilar())
        
    return pila_resultado

pila = Pila()
pila.apilar(2)
pila.apilar(3)
pila.apilar(4)
pila.apilar(6)
pila.apilar(11)
pila.apilar(10)

resultado = apilar_pares(pila)
while not resultado.esta_vacia():
    print(resultado.desapilar())

        