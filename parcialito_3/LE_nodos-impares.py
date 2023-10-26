"""Ejercicio 113 lista-enlazada

Implementar un método para una implementación de ListaEnlazada con referencia únicamente al primer nodo

que devuelve una nueva lista enlazada compuesta por los elementos que se encuentran en las posiciones impares de la original.

Por ejemplo, para L = [3,1,6,8,9] el método debe devolver [1,8]."""

class _Nodo:

    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)

class ListaEnlazada:

    def nodos_impares(self):

        actual = self.prim.prox
        contador = 1
        lista = ListaEnlazada()

        while actual.prox:

            if lista.prim == None:

                if contador%2 == 1:
                    nuevo = _Nodo(actual.dato)
                    lista.prim = nuevo
                    contador += 1
                    actual = actual.prox
                else:
                    contador += 1
                    actual = actual.prox
            
            else:

                actual_lista = lista.prim

                if contador%2 == 1:
                    nuevo = _Nodo(actual.dato)
                    actual_lista.prox = nuevo
                    contador += 1
                    actual = actual.prox
                else:
                    contador += 1
                    actual = actual.prox
        
        return lista
        
        
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
l1.append(3)
l1.append(1)
l1.append(6)
l1.append(8)
l1.append(9)
print(l1)
print(l1.nodos_impares())
