"""Ejercicio 118 lista-enlazada

Para una implementación de ListaEnlazada con referencia únicamente al primer nodo implementar la primitiva suma_acumulativa()

que devuelva una nueva lista (del mismo largo) tal que el nodo i de la nueva lista contenga la suma acumulativa de los elementos de la lista original hasta el nodo i.

Por ejemplo: Si lista tiene los elementos 1, 2, 3, 4, lista.suma_acumulativa() devuelve una nueva ListaEnlazada con 1, 3, 6, 10."""


class _Nodo:

    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)

class ListaEnlazada:

    def acumulativa(self):
        actual = self.prim
        nueva = ListaEnlazada()
        nueva.prim = _Nodo(actual.dato)
        nueva_actual = nueva.prim
        resultado = actual.dato
        actual = actual.prox

        while actual:
            resultado += actual.dato
            nueva_actual.prox = _Nodo(resultado)
            nueva_actual = nueva_actual.prox
            actual = actual.prox

        return nueva


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
print(le)
lista = le.acumulativa()
print(lista)
print(le)