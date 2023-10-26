"""Ejercicio 111 lista-enlazada

Implementar el método reduce dada una implementación de ListaEnlazada con referencia únicamente al primer nodo. 
Este método debe recibir una función y devolver el resultado de dicha reducción a la ListaEnlazada. Ejemplos:

Para [1,2,3] y la función sumar debe devolver 6, ya que (1+2) + 3 = 6
Para [1,2,3] y la función restar debe devolver -4, ya que (1-2) - 3 = -4
Para [1] y la función restar debe devolver 1
Para [] y la función sumar debe lanzar una excepción"""

class ListaEnlazada:


    def reduce(self, funcion):

        if self.__len__() == 1:
            return
        if not self.prim:
            raise Exception("La lista está vacia")

        actual = self.prim
        resultado = actual.dato
        
        while actual.prox:
            resultado = funcion(resultado, actual.prox.dato)
            actual = actual.prox
        self.prim = _Nodo(resultado)


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

def funcion(x, y):
    return x + y


lista = ListaEnlazada()
lista.append(1)
lista.append(2)
lista.append(3)
print(lista)
lista.reduce(funcion)
print(lista)


