"""Ejercicio 129 pilas

Escribir una función que reciba una pila de números y elimine de la misma los elementos consecutivos que estén repetidos.

La función debe actuar in place sobre la pila que recibe por parámetro. Por ejemplo:

remover_duplicados_consecutivos(Pila([2, 5, 8, 8, 8, 3, 3, 2, 3, 3, 3, 1, 8, 7])) → Pila([2, 5, 8, 3, 2, 3, 1, 8, 7])
En caso afirmativo, Indicar el orden en que se efectuaron las operaciones. En caso contrario, justificar."""

from Pila2 import Pila

def remover_duplicados_consecutivos(pila):

    pila_aux = Pila()
    pila_aux.apilar(pila.desapilar())
    while not pila.esta_vacia():
        dato = pila_aux.ver_tope()
        if dato == pila.ver_tope():
            pila.desapilar()
        else:
            pila_aux.apilar(pila.desapilar())

    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())

pila = Pila()

pila.apilar_muchos((7,8,1,3,3,3,2,3,3,8,8,8,5,2))

remover_duplicados_consecutivos(pila)

print(pila)


