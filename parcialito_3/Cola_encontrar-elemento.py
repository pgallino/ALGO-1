"""Ejercicio 151 colas

Escribir una función que, dada una cola y un elemento, devuelva un booleano que indique si el elemento se encuentra o no en la cola.
La cola debe quedar en su estado original."""

from Cola2 import Cola

def encontrar_elemento(cola, elemento):

    cola_aux = Cola()
    dato = None
    while not cola.esta_vacia():
        cosito = cola.desencolar()
        cola_aux.encolar(cosito)
        if cosito == elemento:
            dato = "está"
    
    while not cola_aux.esta_vacia():
        cola.encolar(cola_aux.desencolar())

    if dato:
        return True
    return False

cola = Cola()
cola.encolar_muchos((1,2,3,4,5,6,7,8))
print(cola)
print(encontrar_elemento(cola, 9))
print(cola)
        
