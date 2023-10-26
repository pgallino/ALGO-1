"""Ejercicio 110 lista-enlazada
Se cuenta con una implementación de ListaEnlazada con únicamente una referencia al primer nodo. 

Se pide implementar un método unir_medio, que dada una segunda lista enlazada, la inserte en el medio de la original.

Ejemplo: para las listas a→b→c→d y e→f→g, el resultado debe ser a→b→e→f→g→c→d.

No se puede recorrer ninguna lista más de una vez. Al finalizar la ejecución, la segunda lista debe quedar vacía."""

class _Nodo:

    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)

class ListaEnlazada:

    def unir_medio(self, otra):

        medio = self.__len__() // 2
        contador = 0

        actual = self.prim
        
        while actual.prox:

            if contador == medio - 1:
                actual_otra = otra.prim
                while actual_otra.prox:
                    actual_otra = actual_otra.prox

                actual_otra.prox = actual.prox
                actual.prox = otra.prim
                otra.prim = None
                break
            
            else:
                actual = actual.prox
                contador += 1

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
l1.append("c")
l1.append("d")
l1.append("e")
print(l1)
l2 = ListaEnlazada()
l2.append("e")
l2.append("f")
l2.append("g")
print(l2)
l1.unir_medio(l2)
print(l1)
print(l2)