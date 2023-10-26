
"""Crear una clase PilaConMaximo que soporte las operaciones de Pila 

(apilar(elemento), desapilar() y ver_tope()), y además incluya el método obtener_maximo() en tiempo constante.

"""
import Pila

class _Nodo:

    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

class PilaConMaximo:

    def obtener_maximo(self):
        maximo = self.maximos.tope.dato
        return maximo

    def __init__(self):

        self.maximos = Pila.Pila()
        self.contenido = Pila.Pila()
        self.tope = None

    def apilar(self, dato):
        nodo = _Nodo(dato, self.tope)
        self.tope = nodo
        if self.maximos.tope == None:
            self.maximos.apilar(dato)
        elif dato >= self.maximos.tope.dato:
            self.maximos.apilar(dato)

    def desapilar(self):

        if self.esta_vacia():
            raise ValueError("pila vacía")
        dato = self.tope.dato
        self.tope = self.tope.prox
        if dato == self.maximos.tope.dato:
            self.maximos.desapilar()
        return dato
    
    def ver_tope(self):
        '''
        Devuelve el elemento que está en el tope de la pila.
        Pre: la pila NO está vacía.
        '''
        if self.esta_vacia():
            raise ValueError("pila vacía")
        return self.tope.dato

    def esta_vacia(self):
        '''
        Devuelve True o False según si la pila está vacía o no
        '''
        return self.tope is None