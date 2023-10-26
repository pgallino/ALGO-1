"""Ejercicio 135 pilas
Dada una pila de enteros, escribir una función que determine si es piramidal. 

Una pila de enteros es piramidal si cada elemento es menor a su elemento inferior (el elemento inferior es el siguiente en el sentido hacia la base de la pila). 

Al finalizar la ejecución, la pila debe quedar en el mismo estado con el que empezó."""

from Pila import Pila

def determinar_piramidal(pila):

    pila_aux = Pila()
    dato = 0

    while not pila.esta_vacia():

        if pila_aux.esta_vacia():

            pila_aux.apilar(pila.desapilar())
            anterior = pila_aux.ver_tope()
        else:
            if anterior > pila.ver_tope():
                dato += 1
                break

            else:
                pila_aux.apilar(pila.desapilar())
                anterior = pila_aux.ver_tope()

    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())

    if dato == 1:
        return False

    return True


pila = Pila()
pila.apilar(9)
pila.apilar(6)
pila.apilar(3)
pila.apilar(1)
print(determinar_piramidal(pila))
while not pila.esta_vacia():
    print(pila.desapilar())


