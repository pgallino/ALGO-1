"""Ejercicio 125 lista-enlazada

Para una implementación de una ListaEnlazada que posee únicamente una referencia al primer nodo,

se pide implementar una nueva primitiva que modifique la lista de tal forma que el menor elemento se encuentre al comienzo de la misma,

manteniendo el orden relativo del resto de los elementos.

Importante: El método no debe recorrer la lista más de una vez.

Ejemplos:

3 -> 5 -> 4 -> 2 -> 1   =>   1 -> 3 -> 5 -> 4 -> 2
5 -> 6 -> 2 -> 3 -> 7   =>   2 -> 5 -> 6 -> 3 -> 7
3 -> 4 -> 5 -> 6 -> 7   =>   3 -> 4 -> 5 -> 6 -> 7"""

class _Nodo:

    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)

class ListaEnlazada:

    def menor_primero(self):

        actual = self.prim 
        mas_chico = _Nodo(self.prim.dato)
        numero_mas_chico = mas_chico.dato

        while actual.prox:

            if actual.prox.dato < numero_mas_chico:
                numero_mas_chico = actual.prox.dato
                mas_chico = _Nodo(numero_mas_chico)
                anterior = actual
                siguiente = actual.prox.prox
                actual = actual.prox
            else:
                actual = actual.prox

        if numero_mas_chico != self.prim.dato:

            mas_chico.prox = self.prim
            self.prim = mas_chico
            anterior.prox = siguiente
        
    
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
l1.append(5)
l1.append(4)
l1.append(2)
l1.append(1)
print(l1)
l1.menor_primero()
print(l1)


l2 = ListaEnlazada()
l2.append(5)
l2.append(6)
l2.append(2)
l2.append(3)
l2.append(7)
print(l2)
l2.menor_primero()
print(l2)

l3 = ListaEnlazada()
l3.append(3)
l3.append(4)
l3.append(5)
l3.append(6)
l3.append(7)
print(l3)
l3.menor_primero()
print(l3)

