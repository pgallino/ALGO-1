class ListaEnlazada:

    def invertir(self):
        '''
        invierte la listaEnlazada
        '''
        anterior = self.prim
        actual = self.prim.prox
        final = anterior

        while actual:

            nodo_nuevo = _Nodo(actual.dato)
            nodo_nuevo.prox = self.prim
            self.prim = nodo_nuevo
            final.prox = actual.prox
            anterior = actual
            actual = actual.prox
        
            


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