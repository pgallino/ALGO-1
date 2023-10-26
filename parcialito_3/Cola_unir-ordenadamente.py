"""Ejercicio 149 colas

Escribir una función que reciba dos colas de números enteros (que fueron encolados originalmente de menor a mayor)

y devuelva una nueva cola con los elementos de ambas, ordenada también de menor a mayor. 

Las colas no necesariamente tienen la misma cantidad de elementos, y NO hace falta dejarlas como se recibieron. 

Por ej, si se reciben c1 = [5,2,1] y c2 = [4,1], debe devolver [5,4,2,1,1] (donde 5 y 4 son los ultimos de cada cola original)."""

from Cola2 import Cola

def unir_ordenadamente(cola1, cola2):

    cola_resultado = Cola()

    while not cola1.esta_vacia() and not cola2.esta_vacia():

        dato1 = cola1.ver_frente()
        dato2 = cola2.ver_frente()
        if dato1 > dato2:
            cola_resultado.encolar(cola2.desencolar())
        elif dato1 < dato2:
            cola_resultado.encolar(cola1.desencolar())
        else:
            cola_resultado.encolar(cola1.desencolar())
            cola_resultado.encolar(cola2.desencolar())
        
    while not cola1.esta_vacia():
        cola_resultado.encolar(cola1.desencolar())
    
    while not cola2.esta_vacia():
        cola_resultado.encolar(cola2.desencolar())

    return cola_resultado

cola1 = Cola()
cola2 = Cola()
cola1.encolar_muchos((1,2,5))
print(cola1)
cola2.encolar_muchos((1,4))
print(cola2)
cola = unir_ordenadamente(cola1, cola2)
print(cola)