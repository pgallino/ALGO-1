"""Ejercicio 116 lista-enlazada

Implementar el método merge() para una implementación de ListaEnlazada con referencia únicamente al primer nodo. 
Éste método recibe otra ListaEnlazada por parámetro y tiene como precondición que ambas tienen a todos sus elementos ordenados. 
El método debe devolver una nueva lista enlazada que contenga a los elementos de las dos en orden. Ejemplos:

L1: [3,5,9], L2: [1,2,6,10] -> [1,2,3,5,6,9,10]"""

class _Nodo:

    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)

class ListaEnlazada:

    def merge(self, otra):

        resultado = ListaEnlazada()
        actual = self.prim
        actual_otra = otra.prim

        while actual.prox and actual_otra.prox:

            if resultado.prim == None:

                if actual.dato > actual_otra.dato:
                    nuevo = _Nodo(actual_otra.dato)
                    resultado.prim = nuevo
                    actual_otra = actual_otra.prox
                    actual_res = resultado.prim
                elif actual.dato < actual_otra.dato:
                    nuevo = _Nodo(actual.dato)
                    resultado.prim = nuevo
                    actual = actual.prox
                    actual_res = resultado.prim
                else:
                    nuevo = _Nodo(actual.dato)
                    resultado.prim = nuevo
                    actual = actual.prox
                    actual_otra = actual_otra.prox
                    actual_res = resultado.prim
            
            else:
                    
                if actual.dato > actual_otra.dato:
                    nuevo = _Nodo(actual_otra.dato)
                    actual_res.prox = nuevo
                    actual_res = actual_res.prox
                    actual_otra = actual_otra.prox
                elif actual.dato < actual_otra.dato:
                    nuevo = _Nodo(actual.dato)
                    actual_res.prox = nuevo
                    actual_res = actual_res.prox
                    actual = actual.prox
                else:
                    nuevo = _Nodo(actual.dato)
                    actual_res.prox = nuevo
                    actual_res = actual_res.prox
                    actual = actual.prox
                    actual_otra = actual_otra.prox

        if actual.prox == None:
            while actual_otra:
                nuevo = _Nodo(actual_otra.dato)
                actual_res.prox = nuevo
                actual_res = actual_res.prox
                actual_otra = actual_otra.prox
        else:
            while actual:
                nuevo = _Nodo(actual.dato)
                actual_res.prox = nuevo
                actual_res = actual_res.prox
                actual = actual.prox
                
        return resultado

                


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
l1.append(9)
l2 = ListaEnlazada()
l2.append(1)
l2.append(2)
l2.append(6)
l2.append(9)
l2.append(10)
print(l1)
print(l2)
print(l1.merge(l2))