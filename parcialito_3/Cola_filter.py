"""Ejercicio 152 colas

Escribir una función cola_filter(cola, f) que reciba una cola y una función por parámetro

y devuelva una nueva cola que contenga sólo los elementos para los cuales la función aplicada a ellos devuelva True. 

No es necesario que la cola original quede en su estadio inicial."""

from Cola2 import Cola

def cola_filter(cola, f):

    cola_resultado = Cola()
    while not cola.esta_vacia():
        dato = cola.desencolar()
        if f(dato):
            cola_resultado.encolar(dato)
        
    return cola_resultado

def es_par(n):
    if n%2 == 0:
        return True
    return False

cola = Cola()
cola.encolar_muchos((2,4,2,7,2,4,6,8,3,1,3,5))
print(cola)
cola2 = cola_filter(cola, es_par)
print(cola2)