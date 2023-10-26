"""Ejercicio 143 colas lista-enlazada

Implementar para la ListaEnlazada el método distribuir_en_colas(k), que recibe por parámetro un número entero k mayor a 1.

Este nuevo método debe devolver k nuevas colas con los elementos de la lista distribuidos de forma alternada, respetando el orden relativo de los elementos 

(los k elementos que están al principio de la lista quedarían al frente de cada una de las colas). Ejemplos:

L = [a b c d e f g] → L.distribuir(3) → [Cola([a d g]), Cola([b e]), Cola([c f])]
L = [a b c] → L.distribuir(4) → [Cola([a]), Cola([b]), Cola([c]), Cola([])]"""

from Cola2 import Cola

class _Nodo:

    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)

class ListaEnlazada:

    def distribuir_en_colas(self,k):

        colas = []

        for i in range(k):
            colas.append(Cola())

        actual = self.prim

        while actual:

            for i in range(k):
                colas[i].encolar(actual.dato)
                if actual.prox == None:
                    actual = None
                    break
                actual = actual.prox

        return colas


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
le.append("c")
le.append("d")
le.append("e")
le.append("f")
le.append("g")
lista = le.distribuir_en_colas(3)

for cola in lista:
    print(cola)