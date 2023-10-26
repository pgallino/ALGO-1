"""Ejercicio 121 lista-enlazada

Se tiene una clase ListaEnlazada cuya implementación cuenta únicamente con una referencia al primer nodo, que contiene números ordenados de forma ascendente. 

Se pide escribir un método de la clase ListaEnlazada que la modifique eliminando sus elementos repetidos. 

No se pueden utilizar otros métodos de la lista ni estructuras auxiliares."""

class _Nodo:

    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)

class ListaEnlazada:

    def eliminar_repetidos(self):

        actual = self.prim

        while actual.prox:

            if actual.prox.prox == None and actual.dato == actual.prox.dato:
                actual.prox = None
                break

            elif actual.dato == actual.prox.dato:  #si son iguales no avanzo porque el siguiente tambien puede ser repetido
                actual.prox = actual.prox.prox
            else:
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
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(4)
l1.append(4)
l1.append(6)
l1.append(6)
l1.append(7)
l1.append(8)
l1.append(9)
l1.append(9)
print(l1)
l1.eliminar_repetidos()
print(l1)
