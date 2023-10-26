"""Ejercicio 120 lista-enlazada
Teniendo una ListaEnlazada implementada como solo una referencia al primer nodo, se pide implementar el método __mul__ 

que reciba un número entero n y devuelva una nueva lista enlazada con los mismos elementos repetidos n veces.

Aclaración: la nueva lista debe ser recorrida una sola vez (es decir, no se puede utilizar el método append().

Ejemplo:

L: [a,b] → L * 3 → [a,b,a,b,a,b]"""

class _Nodo:

    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)

class ListaEnlazada:

    def __mul__(self, n):

        nueva_lista = ListaEnlazada()

        for i in range(n):

            actual = self.prim

            while actual:
                if nueva_lista.prim == None:
                    nueva_lista.prim = _Nodo(actual.dato)
                    nueva_lista_actual = nueva_lista.prim
                else:
                    nueva_lista_actual.prox = _Nodo(actual.dato)
                    nueva_lista_actual = nueva_lista_actual.prox
                actual = actual.prox
                nueva_lista.cant += 1

        return nueva_lista


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

le = ListaEnlazada()
le.append("a")
le.append("b")
print(le * 5)
print(le)