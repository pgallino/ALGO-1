from Pila2 import Pila

"""funcion recursiva que cuenta la cantidad de elementos de una pila y no altera su contenido"""

def contar_elementos_pila1(pila):
    
    if pila.esta_vacia():
        return 0 

    elemento = pila.desapilar()

    cantidad= 1 + contar_elementos_pila(pila)        #primero obtiene la cantidad

    pila.apilar(elemento)                            #el elemento quedó guardado en su propio marco de la llamada recursiva, entonces se apila despues de haber contado todos los elementos

    return cantidad

def _contar_elementos_pila(pila, lista):              #forma nefashta
    
    if pila.esta_vacia():
        return 0
    
    lista.append(pila.desapilar())

    return _contar_elementos_pila(pila, lista) + 1

def contar_elementos_pila(pila):
    lista = []
    cantidad = _contar_elementos_pila(pila, lista)
    for i in range(cantidad - 1, -1, -1):
        pila.apilar(lista[i])
    return cantidad

pila = Pila()

pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.apilar(4)

print(pila)

print(contar_elementos_pila(pila))

print(pila)

