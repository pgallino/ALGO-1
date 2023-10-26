# 2. Escribir una función que reciba por parámetro dos pilas y modifique su
# contenido de manera que los elementos de la primer pila queden en la
# segunda, y los de la segunda en la primera manteniendo el orden original de
# los elementos. Como estructuras auxiliares, se pueden utilizar únicamente
# pilas y/o colas.


from tda import Pila, Cola

# Completar la siguiente funcion
def intercambiar_pilas(pila1, pila2):
    
    pila1_aux = Pila()
    pila2_aux = Pila()

    while not pila1.esta_vacia():
        pila1_aux.apilar(pila1.desapilar())
    
    while not pila2.esta_vacia():
        pila2_aux.apilar(pila2.desapilar())
    
    while not pila1_aux.esta_vacia():
        pila2.apilar(pila1_aux.desapilar())
    
    while not pila2_aux.esta_vacia():
        pila1.apilar(pila2_aux.desapilar())


p1 = Pila([4, 5, 6, 9])
p2 = Pila([1, 3])

intercambiar_pilas(p1, p2)

assert p1 == Pila([1, 3])
assert p2 == Pila([4, 5, 6, 9])
