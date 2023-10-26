# 1. Dada una pila con números, escribir una función **recursiva** que calcule el
# producto de los mismos. La pila debe quedar en su estado original al final de
# la ejecución.


from tda import Pila, Cola

# Completar la siguiente funcion
def calcular_producto(pila):

    if pila.esta_vacia():
        return 1
    
    dato = pila.desapilar()
    
    valor = calcular_producto(pila) * dato

    pila.apilar(dato)

    return valor



p = Pila([2, 3, 4, 6])
assert calcular_producto(p) == 144
assert p == Pila([2, 3, 4, 6]), 'pila no quedo en su estado original'

