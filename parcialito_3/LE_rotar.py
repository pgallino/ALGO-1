"""Ejercicio 124 lista-enlazada

Escribir un método de ListaEnlazada que permita rotar la lista en N posiciones. El método debe modificar la lista y no devolver una nueva. 

Además, el método no debe recorrer la lista N veces si hay que hacer una rotación de N elementos. Asumir que N siempre es >= 0. 

La implementación de LE contiene una referencia al primer nodo y un atributo con la longitud. Ejemplo: dada la LE [1, 2, 3, 4, 5, 6, 7, 8] (len = 8)

le.rotar(0) -> [1, 2, 3, 4, 5, 6, 7, 8]
le.rotar(2) -> [3, 4, 5, 6, 7, 8, 1, 2]
le.rotar(11) -> [4, 5, 6, 7, 8, 1, 2, 3]
le.rotar(10) -> [3, 4, 5, 6, 7, 8, 1, 2]"""

class _Nodo:

    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)

class ListaEnlazada:

    def rotar(self,N):

        if N == self.cant or N == 0 or not self.prim or self.cant == 1:
            return
        else:
            if N > self.cant:
                N %= self.cant

            if N == 0:
                return

            actual = self.prim
            ultimo_prox = actual

            for i in range(N - 1):
                actual = actual.prox
            nuevo_ultimo = actual
            nuevo_primero = actual.prox

            while actual.prox:
                actual = actual.prox
            
            self.prim = nuevo_primero
            nuevo_ultimo.prox = None
            actual.prox = ultimo_prox

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
le.append(1)
le.append(2)
le.append(3)
le.append(4)
le.append(5)
print(le)
le.rotar(25)
print(f"rotada 25 pos: {le}")

le = ListaEnlazada()
le.append(1)
le.append(2)
le.append(3)
le.append(4)
le.append(5)
le.append(6)
le.append(7)
le.append(8)
print(le)
le.rotar(2)
print(f"rotada 2 pos: {le}")

le = ListaEnlazada()
le.append(1)
le.append(2)
le.append(3)
le.append(4)
le.append(5)
le.append(6)
le.append(7)
le.append(8)
print(le)
le.rotar(11)
print(f"rotada 11 pos: {le}")

le = ListaEnlazada()
le.append(1)
le.append(2)
le.append(3)
le.append(4)
le.append(5)
le.append(6)
le.append(7)
le.append(8)
print(le)
le.rotar(10)
print(f"rotada 10 pos: {le}")