class ListaCircular:

    def remove(self, x):
        '''
        DOC: Completar
        '''
        
        if self.prim:

            actual = self.prim
            contador = 0
    
            if actual.dato == x:
                while actual.prox != self.prim:
                    actual = actual.prox
                    
                self.prim = self.prim.prox
                actual.prox = self.prim
                self.cant -= 1
    
            else:
                while actual.prox.dato != x:
                    actual = actual.prox
                    contador += 1
                    if contador + 1 > self.__len__():
                        raise ValueError
                
                if contador + 1 == self.__len__():
                    actual.prox = self.prim
                    self.cant -= 1
                else:
                    actual.prox = actual.prox.prox
                    self.cant -= 1

            


    def insert(self, i, x):

        '''
        DOC Completar
        '''
        
        if self.prim:
            actual = self.prim
            nuevo = _Nodo(x)
    
            if i == 0:
                while actual.prox.prox != self.prim:
                    actual = actual.prox
                
                nuevo.prox = self.prim
                self.prim = nuevo
                actual.prox.prox = nuevo
    
    
            else:
                
                if i > self.__len__():
                    
                    i = i % self.__len__()
    
                for nodo in range(1, i):
                    actual = actual.prox
                nuevo.prox = actual.prox
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

    def __str__(self):
        
        lista = "["
        actual = self.prim
        while actual.prox != self.prim:
            lista += f"{actual.dato}, "
            actual = actual.prox

        lista += f"{actual.dato}, "
        lista = lista.rstrip(", ") + "]"
        return lista

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


class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox
    
    def __str__(self):
        return str(self.dato)