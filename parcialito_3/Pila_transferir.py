"""Ejercicio 131 pilas

Escribir una funcion transferir(p1, p2) que recibe dos pilas y transfiere todos los elementos de p1 al tope de p2,

de forma tal que queden en el mismo orden (es decir, el elemento que estaba inicialmente en el tope de p1 debe quedar en el tope de p2).

La pila p1 debe quedar vacía al finalizar la función."""

from Pila import Pila

def transferir(pila1, pila2):
    
    pila_aux = Pila()
    while not pila1.esta_vacia():
        pila_aux.apilar(pila1.desapilar())

    while not pila_aux.esta_vacia():
        pila2.apilar(pila_aux.desapilar())

pila1 = Pila()
pila1.apilar(1)
pila1.apilar(2)
pila1.apilar(3)
pila1.apilar(4)
pila2 = Pila()
pila2.apilar(-4)
pila2.apilar(-3)
pila2.apilar(-2)
pila2.apilar(-1)
pila2.apilar(0)
transferir(pila1, pila2)
while not pila2.esta_vacia():
    print(pila2.desapilar())