from Pila import Pila
from Cola import Cola

def reemplazar(pila, valor_viejo, valor_nuevo):

    pila_aux = Pila()

    while not pila.esta_vacia():
        dato = pila.desapilar()
        if dato == valor_viejo:
            pila_aux.apilar(valor_nuevo)
        else:
            pila_aux.apilar(dato)
    
    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())