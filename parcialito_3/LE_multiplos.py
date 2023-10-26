"""Ejercicio 114 lista-enlazada
Implementar el método downsample(k) para una implementación de ListaEnlazada con referencia únicamente al primer nodo.
Este método debe eliminar todo elemento de la lista que ocupe una posición que no sea múltiplo del número k pasado por parámetro (k > 1).

Ejemplos:

L: [0, 1, 2, 3, 4, 5]                  → L.downsample(2) → L: [0, 2, 4]
L: ['a', 'b', 'c', 'd', 'e', 'f', 'g'] → L.downsample(4) → L: ['a', 'e'] """

class ListaEnlazada:


    def downsample(self, k):
        
        if not self.prim:
            return

        principal = self.prim
        actual = self.prim.prox
        contador = 1

        while actual.prox:

            if contador%k == 0:
                
                principal.prox = actual
                principal = actual
                actual = actual.prox
                contador += 1

            else:
                contador += 1
                actual = actual.prox
                
        if contador%k == 0:
            principal.prox = actual
            
        else:
            principal.prox = None
        
        self.cant = (self.cant) // k
        
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

class _Nodo:

    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)

lista = ListaEnlazada()
lista.append("a")
lista.append("b")
lista.append("c")
lista.append("d")
lista.append("e")
lista.append("f")
lista.append("g")
print(lista)
lista.downsample(4)
print(lista)
print(lista.__len__())

lista2 = ListaEnlazada()
lista2.append(0)
lista2.append(1)
lista2.append(2)
lista2.append(3)
lista2.append(4)
lista2.append(5)
print(lista2)
lista2.downsample(2)
print(lista2)
print(lista2.__len__())