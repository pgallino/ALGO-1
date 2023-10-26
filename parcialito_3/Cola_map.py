"""Ejercicio 147 colas
Escribir una función cola_map(cola, f) que reciba por parámetro una cola y una función,

y devuelva una nueva cola aplicando sucesivamente la función f a cada elemento de la cola original 

(que debe quedar en el mismo estado con el que empezó al finalizar la ejecución de la función)."""

from Cola2 import Cola

def cola_map(cola, f):

    cola_resultado = Cola()
    cola_aux = Cola()
    while not cola.esta_vacia():
        dato = cola.desencolar()
        cola_resultado.encolar(f(dato))
        cola_aux.encolar(dato)

    while not cola_aux.esta_vacia():
        cola.encolar(cola_aux.desencolar())
        
    return cola_resultado

def elevar(n):
    return n**2

cola = Cola()
cola.encolar_muchos((2,4,2,7))
print(cola)
cola2 = cola_map(cola, elevar)
print(cola2)
print(cola)