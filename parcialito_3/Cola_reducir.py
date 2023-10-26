"""Del segundo recuperatorio del tercer parcialito del primer cuatrimestre de 2014
5. Escribir una funcion reducir que reciba por parametro una cola y una funcion f de dos
parametros, y aplique sucesivamente la funcion f a los dos primeros elementos de la cola (luego
de desencolarlos) y encole el resultado, hasta que solo quede un elemento. La funcion reducir
debe devolver el unico elemento restante en la cola."""

from Cola2 import Cola

def reducir_cola(cola, f):

    while True:
        dato1 = cola.desencolar()
        if cola.esta_vacia():
            break
        dato2 = cola.desencolar()
        cola.encolar(f(dato1, dato2))

    return dato1

def suma(x,y):
    return x + y

cola = Cola()
cola.encolar_muchos((1,2,3,4,5,6,))
print(cola)
print(reducir_cola(cola,suma))