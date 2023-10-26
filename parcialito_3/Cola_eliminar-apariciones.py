"""Ejercicio 144 colas

Implementar una función que reciba una cola y un elemento y modifique la cola original eliminando todas las apariciones del elemento recibido por parámetro. 

El resto de los elementos deben preservar el orden original en el que estaban."""


from Cola2 import Cola

def eliminar_apariciones(cola, elemento):

    cola_aux = Cola()
    while not cola.esta_vacia():
        dato = cola.desencolar()
        if dato != elemento:
            cola_aux.encolar(dato)

    while not cola_aux.esta_vacia():
        cola.encolar(cola_aux.desencolar())

cola = Cola()
cola.encolar_muchos((1,2,54,2,3,15,54,2,5,54))
print(cola)
eliminar_apariciones(cola, 54)
print(cola)



        