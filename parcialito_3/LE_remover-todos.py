class ListaEnlazada:

    def remover_todos(self, elem):

        eliminados = 0

        if not self.prim:
            return eliminados

        actual = self.prim
        while actual.prox:
            
            if actual.prox.dato == elem:
                actual.prox = actual.prox.prox
                eliminados += 1
            else:
                actual = actual.prox

        if self.prim.dato == elem:
            self.prim = self.prim.prox
            eliminados += 1

        self.cant -= eliminados
        return eliminados


    def __init__(self):
        # prim es un _Nodo o None
        self.prim = None
        self.cant = 0

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