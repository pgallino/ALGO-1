"""Del recuperatorio del tercer parcialito del primer cuatrimestre de 2012

Escribir un metodo que invierta una ListaEnlazada utilizando una Pila como estructura auxiliar

y considerando que lista solo tiene una referencia al primer nodo."""

from Pila2 import Pila

class _Nodo:

    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)

class ListaEnlazada:

    def invertir(self):

        pila = Pila()

        actual = self.prim
        while actual:
            pila.apilar(_Nodo(actual.dato))
            if not actual.prox:
                break
            actual = actual.prox

        self.prim = None
        
        while not pila.esta_vacia():
            if self.prim == None:
                self.prim = pila.desapilar()
                actual = self.prim
            else:
                actual.prox = pila.desapilar()
                actual = actual.prox
                

    def __init__(self):
        # prim es un _Nodo o None
        self.prim = None
        self.cant = 0

    def __str__(self):
        lista = "["
        actual = self.prim
        while actual:
            lista += f"{actual.dato}, "
            actual = actual.prox
        lista = lista.rstrip(", ") + "]"
        return lista

    def append(self, dato):
        nuevo = _Nodo(dato)
        if not self.prim:
            self.prim = nuevo
        else:
            act = self.prim
            while act.prox:
                act = act.prox
            # act es el ultimo nodo
            act.prox = nuevo
        self.cant += 1


    def __len__(self):
        return self.cant

l1 = ListaEnlazada()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
l1.append(6)
l1.append(7)
l1.append(8)
print(l1)
l1.invertir()
print(l1)