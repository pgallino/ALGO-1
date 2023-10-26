"""Ejercicio 148 colas

Escribir una función cola_dividir(cola, f) que reciba por parámetro una cola y una función, 

y devuelva dos colas: una que contenga los elementos de la cola original para los cuales f(elemento) → True (respetando el orden), 

y otra con los elementos para los cuales la función dio False (también respetando el orden). 

La cola original debe quedar en el mismo estado con el que empezó al finalizar la ejecución de la función."""

from Cola2 import Cola

def cola_dividir(cola, f):

    cola_true = Cola()
    cola_false = Cola()
    cola_aux = Cola()

    while not cola.esta_vacia():

        dato = cola.desencolar()
        
        if f(dato) == True:
            cola_true.encolar(dato)
        
        elif f(dato) == False:
            cola_false.encolar(dato)
        
        cola_aux.encolar(dato)

    while not cola_aux.esta_vacia():
        cola.encolar(cola_aux.desencolar())

    return cola_true, cola_false

def es_par(n):
    if n%2 == 0:
        return True
    return False

cola = Cola()
print(cola)
cola.encolar_muchos((1,4,1,2,5,2,3,7,3,8,2,3))
print(cola)
cola_true , cola_false = cola_dividir(cola, es_par)
print(cola_true)
print(cola_false)
print(cola)
