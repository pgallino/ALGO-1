"""Ejercicio 120 lista-enlazada

Teniendo una ListaEnlazada implementada como solo una referencia al primer nodo, se pide implementar el método __mul__ que reciba un número entero n

y devuelva una nueva lista enlazada con los mismos elementos repetidos n veces.

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

        lista_aux = ListaEnlazada()

        while lista_aux.cant != (self.cant) * n:

            actual = self.prim
            
            while actual:

                if lista_aux.prim == None:
                    nuevo = _Nodo(actual.dato)
                    lista_aux.prim = nuevo
                    actual_aux = lista_aux.prim

                else:
                    nuevo = _Nodo(actual.dato)
                    actual_aux.prox = nuevo
                    actual_aux = actual_aux.prox

                actual = actual.prox
                lista_aux.cant += 1

        return lista_aux
        
        
        
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
l1.append("a")
l1.append("b")
print(l1)
l2 = l1 * 3
print(l2)
print(l2.__len__())



