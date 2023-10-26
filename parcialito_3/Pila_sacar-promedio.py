"""Ejercicio 132 pilas

Implementar una función que calcule el promedio de los elementos de una pila de números que recibe por parámetro. 

La pila debe quedar en el mismo estado en el que fue recibida (con los mismos elementos y en el mismo orden)."""

from Pila import Pila

def sacar_promedio(pila):
    resultado = 0
    cantidad = 0
    pila_aux = Pila()

    while not pila.esta_vacia():
        resultado += pila.ver_tope()
        cantidad += 1
        pila_aux.apilar(pila.desapilar())

    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())

    return resultado / cantidad

pila = Pila()
pila.apilar(4)
pila.apilar(5)
pila.apilar(2)
pila.apilar(9)
print(sacar_promedio(pila))
while not pila.esta_vacia():
    print(pila.desapilar())