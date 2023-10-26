class ListaEnlazada:

    def extend(self, lista_aux):

        '''
        a una lista se le añade otra lista
        '''

        if not lista_aux.prim:
            return
        
        primero_aux = lista_aux.prim
        if not self.prim:
            self.prim = _Nodo(primero_aux.dato)
            primero_aux = primero_aux.prox
            ultimo_original = self.prim
            self.cant += 1
        else:
            actual = self.prim
            while actual.prox:
                actual = actual.prox
            ultimo_original = actual 
        
        # Esto estaría mal:
        #  ultimo_L1.prox = lista_enlazada.prim
        
        actual_aux = primero_aux
        while actual_aux:
          nodo_nuevo = _Nodo(actual_aux.dato)
          ultimo_original.prox = nodo_nuevo
          ultimo_original = ultimo_original.prox
          actual_aux = actual_aux.prox
          self.cant += 1

    def extend_2(self, lista_aux):

        '''
        igual que extend pero con append
        '''

        act_aux = lista_aux.prim
        if not act_aux:
            return 
        while act_aux:
           self.append(act_aux.dato)
           act_aux = act_aux.prox

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