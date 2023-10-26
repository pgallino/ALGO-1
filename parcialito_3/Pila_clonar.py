"""Ejercicio 139 pilas colas

Escribir una función clonar_pila, que reciba por parámetro una pila y devuelva una nueva pila con los elementos de la primera manteniendo el orden original.

Nota: la pila recibida debe quedar en su estado original."""


from Cola import Cola
from Pila import Pila

def clonar_pila(pila):
    
    pila_aux = Pila()
    pila_resultado = Pila()

    while not pila.esta_vacia():
        pila_aux.apilar(pila.desapilar())

    while not pila_aux.esta_vacia():
        dato = pila_aux.desapilar()
        pila.apilar(dato)
        pila_resultado.apilar(dato)
    
    return pila_resultado

pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.apilar(4)
pila1 = clonar_pila(pila)
while not pila1.esta_vacia():
    print(pila1.desapilar())

    

