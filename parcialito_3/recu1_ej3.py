# Implementar una función que reciba una pila de números enteros ordenados ascendentemente y determine si todos los números son consecutivos.
# La pila debe preservar su estado inicial.
# Ejemplo:
# >>> consecutivos(Pila(1,2,3,4,5,6))
# True
# >>> consecutivos(Pila(1,2,4,5,6,7))
# False

from tda import Pila, Cola

# Completar la siguiente funcion
def consecutivos(numeros):
    resultado = 1
    aux = Pila()
    anterior = numeros.ver_tope()
    aux.apilar(numeros.desapilar())
    while not numeros.esta_vacia():
        primero = numeros.ver_tope()
        if primero != anterior -1:
            resultado = 2
        anterior = primero
        aux.apilar(numeros.desapilar())
    
    while not aux.esta_vacia():
        numeros.apilar(aux.desapilar())
    
    if resultado == 2:
        return False
    return True

# Pruebas
p1 = Pila()
p2 = Pila()
p1.apilar_desde([1,2,3,4,5,6])
p2.apilar_desde([1,2,4,5,6,7])
assert consecutivos(p1) == True
assert consecutivos(p2) == False
