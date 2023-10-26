class ListaCircular:

    def append(self, dato):

        '''
        append(x): Agrega el elemento x al final de la lista.
        
        '''

        if self.prim == None:
            self.prim = _Nodo(dato)
            self.prim.prox = self.prim
            
        elif self.__len__() == 1:
            actual = self.prim
            nuevo = _Nodo(dato)
            nuevo.prox = self.prim
            actual.prox = nuevo
        
        else:
            actual = self.prim
            while actual.prox != self.prim:
                actual = actual.prox
            
            nuevo = _Nodo(dato)
            nuevo.prox = self.prim
            actual.prox = nuevo
        self.cant += 1
        
        
    def pop(self, i=None):

        '''
        pop(i=None): Elimina el nodo de la posición i y devuelve su dato. 
        
        Si i = None, se elimina el último nodo.

        '''

        actual = self.prim

        if i == None:
            while actual.prox.prox != self.prim:
                actual = actual.prox
            dato = actual.prox.dato
            actual.prox = self.prim
            self.cant -= 1
            return dato
        
        if i == 0:
            while actual.prox != self.prim:
                actual = actual.prox
                
            dato = self.prim.dato
            self.prim = self.prim.prox
            actual.prox = self.prim
            self.cant -= 1
            return dato
                
        else:
            for nodo in range(1, i):
                actual = actual.prox

            dato = actual.prox.dato
            actual.prox = actual.prox.prox
            self.cant -= 1
            return dato



    def __len__(self):
        return self.cant

    def __init__(self):
        # prim es un _Nodo o None
        self.prim = None
        self.cant = 0


class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox