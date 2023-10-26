"""Ejercicio 115 lista-enlazada

Implementar un método para una implementación de ListaEnlazada con referencia únicamente al primer nodo

que reciba una secuencia de números ordenados y sin repeticiones (por ejemplo, la tupla (0, 2, 6, 8)),

y elimine los elementos de la lista enlazada en dichas posiciones, recorriendo la lista enlazada una única vez. 

Si la secuencia de índices a eliminar contiene una posición no válida se deberá lanzar una excepción.

Ejemplos:

L: [ a b c d e ]  →  L.eliminar_posiciones([1, 3])  →  L: [ a c e ]
L: [ a c e ]      →  L.eliminar_posiciones([0, 2])  →  L: [ c ]
L: [ a c e ]      →  L.eliminar_posiciones([0, 3])  →  IndexError"""

class _Nodo:

    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)

class ListaEnlazada:

    def eliminar_posiciones(self, secuencia):

        if self.cant < secuencia[-1]:
            raise  Exception("la lista es mas corta que las posiciones dadas")

        actual = self.prim
        contador = 0

        while actual.prox:

            if contador == 0 and contador in secuencia:

                self.prim = actual.prox
                anterior = self.prim
                actual = actual.prox
                contador += 1

                while contador in secuencia:

                    self.prim = actual.prox
                    anterior = self.prim
                    actual = actual.prox
                    contador += 1



            elif contador in secuencia:

                anterior.prox = actual.prox
                anterior = actual
                actual = actual.prox
                contador += 1

            else:

                anterior = actual
                actual = actual.prox
                contador += 1
            
            if actual.prox == None and contador in secuencia:
                anterior.prox = None
                
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
l1.append(0)
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
l1.append(6)
l1.append(7)
print(l1)
l1.eliminar_posiciones([0,1,2,5])
print(l1)
l1.eliminar_posiciones([0,2])
print(l1)
l2 = ListaEnlazada()
l2.append(0)
l2.append(1)
l2.append(2)
print(l2)
l2.eliminar_posiciones([0,5])