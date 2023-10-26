"""Ejercicio 165 recursion

Dada una Cola cuyas únicas primitivas son encolar y desencolar, escribir una función recursiva que invierta in-place los elementos de la misma. 

No se permite usar estructuras auxiliares."""
from Cola2 import Cola

def invertir_cola(cola):

    if cola.esta_vacia():
        return

    valor = cola.desencolar()

    invertir_cola(cola)

    cola.encolar(valor)

cola = Cola()
cola.encolar_muchos([1,2,3,4,5,6,7,9,11,0])
print(cola)
invertir_cola(cola)
print(cola)