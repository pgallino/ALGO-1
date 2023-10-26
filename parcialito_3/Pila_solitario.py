
"""Crear una clase Carta que contenga un palo y un valor, y una clase Solitario que permita apilar las cartas una arriba de otra.

Solo permite apilar una carta si es de un número inmediatamente inferior y de distinto palo a la carta que está en el tope. 

Si se intenta apilar una carta incorrecta, debe lanzar una excepción."""


class Carta:
    '''
    DOC: Completar
    '''
    def __init__(self, palo, numero):
        self.palo = palo
        self.numero = numero
    
    def comparar_numero(self, otra):
        if self.numero - otra.numero == 1:
            return True
        else:
            return False
    
    def comparar_palo(self, otra):
        if self.palo != otra.palo:
            return True
        else:
            return False


class Solitario:

    '''
    DOC: Completar
    '''
    def __init__(self):
        self.tope = None

    def apilar(self, carta):

        if self.esta_vacia():
            nodo = _Nodo((carta.palo, carta.numero), self.tope)
            self.tope = nodo
        else:
            palo_actual, numero_actual = self.tope.dato
            carta_actual = Carta(palo_actual, numero_actual)
            if carta_actual.comparar_numero(carta) and carta_actual.comparar_palo(carta):
                nodo = _Nodo((carta.palo, carta.numero), self.tope)
                self.tope = nodo
            else:
                raise Exception("Carta inválida")
    
    def esta_vacia(self):
        '''
        Devuelve True o False según si la pila está vacía o no
        '''
        return self.tope is None

class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox