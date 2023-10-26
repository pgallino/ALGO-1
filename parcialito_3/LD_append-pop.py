class ListaDobleEnlazada:

    def append(self, dato):

        '''
        append(x): Agrega el elemento x al final de la lista.

        '''
        nuevo = _Nodo(dato)

        if not self.prim:
            self.prim = nuevo

        else:

            actual = self.prim

            while actual.prox:
                actual = actual.prox
            actual.prox = nuevo
            nuevo.ant = actual

        self.cant += 1



    def pop(self, i=None):

        '''Elimina el nodo de la posición i, y devuelve el dato contenido.
        Si i está fuera de rango, se levanta la excepción IndexError.
        Si no se recibe la posición, devuelve el último elemento.'''

        if i == None:
            i = self.cant - 1

        if i < 0 or i >= self.cant:
            raise IndexError

        if i == 0:

            dato = self.prim.dato
            self.prim = self.prim.prox

        else:
            actual = self.prim
            for pos in range(1, i + 1):
                actual = actual.prox

            dato = actual.dato
            actual.ant.prox = actual.prox
            actual.prox.ant = actual.ant
        self.cant -= 1
        return dato


    def __len__(self):
        return self.cant

    def __init__(self):
        # prim es un _Nodo o None
        self.prim = None
        self.cant = 0


class _Nodo:
    def __init__(self, dato, prox=None, ant=None):
        self.dato = dato
        self.prox = prox
        self.ant = ant