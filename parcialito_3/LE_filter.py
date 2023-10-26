class ListaEnlazada:

    def filter(self, f):

        '''
        recibe una función y devuelve una nueva lista enlazada con los elementos para los cuales la aplicación de f devuelve True
        '''

        l2 = ListaEnlazada()

        actual = self.prim
        
        while actual:

            if f(actual.dato):
                nuevo = _Nodo(actual.dato)
                l2.prim = nuevo
                l2.cant += 1
                actual = actual.prox
                break
            else:
                actual = actual.prox
        
        actual_l2 = l2.prim

        while actual:
            if f(actual.dato):
                nuevo = _Nodo(actual.dato)
                actual_l2.prox = nuevo
                l2.cant += 1
                actual_l2 = actual_l2.prox
                actual = actual.prox
            else:
                actual = actual.prox

        return l2

    def filter_corta(self, f):
        '''
        igual que filter pero mejor
        '''
        l2 = ListaEnlazada()
        actual = self.prim
        actual_l2 = None

        while actual:

            if f(actual.dato) and not actual_l2:  #si actual_l2 no es None, es porque es el primero, tonces ese es prim
                nuevo = _Nodo(actual.dato)
                l2.prim = nuevo    
                actual_l2 = l2.prim
                l2.cant += 1
                
            elif f(actual.dato):
                nuevo = _Nodo(actual.dato)
                actual_l2.prox = nuevo
                actual_l2 = actual_l2.prox
                l2.cant += 1

            actual = actual.prox
        return l2
                
                


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