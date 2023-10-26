"""Del primer recuperatorio del tercer parcialito del primer cuatrimestre de 2014

6. Escribir una funcion que reciba una cola y la cantidad de elementos en la misma,
y devuelva True si los elementos forman un palındromo o False si no.

Por ejemplo:
es palindromo([n, e, u, q, u, e,n], 7) − > True"""

from Cola2 import Cola
from Pila2 import Pila

def es_palindromo(cola, n):

    pila_aux = Pila()
    par = True
    
    if n%2 != 0:
        par = False
        n -= 1
        
    for i in range((n)//2):

        pila_aux.apilar(cola.desencolar())

    if not par:
        cola.desencolar()

    while not pila_aux.esta_vacia():
        if pila_aux.desapilar() != cola.desencolar():
            return False
    
    return True

cola = Cola()
cola.encolar_muchos((True,False,True,True,False,True))
print(cola)
print(es_palindromo(cola,6))


