"""Ejercicio 153 colas
Se encontraron incongruencias en los planes preventivos de la pandemia de COBID20. 
El plan del país lleva una serie de fases a cumplir las cuales estan insertadas en una cola de menor a mayor. 
De alguna manera hay fases intercaladas que no estaban en el plan y se nos exige removerlas.
Se pide entonces escribir una funcion que dada dicha cola de fases, la modifique de forma que sólo quede una serie de fases ordenadas. 
Ejemplo:

Para la cola:
sale <| 1 2 6 3 5 4 5 6 7 |< entra
debería quedar la cola:
sale <| 1 2 6 7 |< entra

Para la cola:
sale <| 1 5 4 3 2 8 |< entra
debería quedar la cola:
sale <| 1 5 8 |< entra"""

from Cola2 import Cola

def ordenar_fases(cola):

    if cola.esta_vacia():
        return

    cola_aux = Cola()

    while not cola.esta_vacia():
        if cola_aux.esta_vacia():
            dato = cola.desencolar()
            anterior = dato
            cola_aux.encolar(dato)
        else:
            dato = cola.desencolar()
            if dato > anterior:
                cola_aux.encolar(dato)
                anterior = dato

    while not cola_aux.esta_vacia():
        cola.encolar(cola_aux.desencolar())

cola = Cola()
cola.encolar_muchos((1,2,6,3,5,4,5,6,7))
print(cola)
ordenar_fases(cola)
print(cola)

cola = Cola()
cola.encolar_muchos((1,5,4,3,2,8))
print(cola)
ordenar_fases(cola)
print(cola)

