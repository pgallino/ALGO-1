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

    def rotar(self, N):

        if N > self.cant:
            N %= self.cant

        if N != 0:


            if N != self.cant:

                lista_aux = ListaEnlazada()

                actual = self.prim
                lista_aux.prim = _Nodo(actual.dato)
                actual = actual.prox
                actual_aux = lista_aux.prim
                
                for i in range(1, N):
                    
                    actual_aux.prox = _Nodo(actual.dato)
                    actual_aux = actual_aux.prox
                    actual = actual.prox

                self.prim = actual

                while actual.prox:
                    actual = actual.prox

                actual.prox = lista_aux.prim

            else:
                actual = self.prim
                nuevo = _Nodo(actual.dato)
                actual = actual.prox
                self.prim = actual
                while actual.prox:
                    actual = actual.prox

                actual.prox = nuevo

        
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
l1.rotar(2)
print(l1)


