"""Ejercicio 111 lista-enlazada
Implementar el método reduce dada una implementación de ListaEnlazada con referencia únicamente al primer nodo.

Este método debe recibir una función y devolver el resultado de dicha reducción a la ListaEnlazada. Ejemplos:

Para [1,2,3] y la función sumar debe devolver 6, ya que (1+2) + 3 = 6
Para [1,2,3] y la función restar debe devolver -4, ya que (1-2) - 3 = -4
Para [1] y la función restar debe devolver 1
Para [] y la función sumar debe lanzar una excepción"""

class _Nodo:

    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)

class ListaEnlazada:

    def reducir(self, f):

        resultado = self.prim.dato
        actual = self.prim.prox

        while actual.prox:
            resultado = f(resultado, actual.dato)
            actual = actual.prox

        return f(resultado, actual.dato)

        


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

def suma(x,y):
    return x-y
    
l1 = ListaEnlazada()
l1.append(1)
l1.append(2)
l1.append(3)
print(l1.reducir(suma))