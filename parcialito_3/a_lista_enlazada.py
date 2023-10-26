class _Nodo:

    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)

class ListaEnlazada:

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


    def pop(self, i=None):

        '''Elimina el nodo de la posición i, y devuelve el dato contenido.
        Si i está fuera de rango, se levanta la excepción IndexError.
        Si no se recibe la posición, devuelve el último elemento.'''

        if i is None:
            i = self.cant - 1
        if i < 0 or i >= self.cant:
            raise IndexError
        if i == 0:
            dato = self.prim.dato
            self.prim = self.prim.prox
        else:
            n_ant = self.prim
            n_act = n_ant.prox
            for pos in range(1,i):
                n_ant = n_act
                n_act = n_ant.prox
            dato = n_act.dato
            n_ant.prox = n_act.prox
        self.cant -= 1
        return dato


    def insert(self, i, x):

        '''Inserta el elemento x en la posición i.
        Si la posición es inválida, levanta IndexError'''

        if i < 0 or i > self.cant:
            raise IndexError
        nuevo = _Nodo(x)
        if i == 0:
            nuevo.prox = self.prim
            self.prim = nuevo
        else:
            n_ant = self.prim
            for pos in range(1, i):
                n_ant = n_ant.prox
            nuevo.prox = n_ant.prox
            n_ant.prox = nuevo
        self.cant += 1


    def remove(self, x):

        '''Borra la primera aparición del valor x en la lista.
        Si x no está en la lista, levanta ValueError.'''

        if self.cant == 0:
            raise ValueError
        if self.prim.dato == x:
            self.prim = self.prim.prox
        else:
            n_ant = self.prim
            n_act = n_ant.prox
            while n_act is not None and n_act.dato != x:
                n_ant = n_act
                n_act = n_ant.prox
            if n_act == None:
                raise ValueError
            n_ant.prox = n_act.prox
        self.cant -= 1
        
    
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

    def __iter__(self):
        return IteradorListaEnlazada(self)}

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

class IteradorListaEnlazada:

    def __init__(self, lista):
        self.lista = lista
        self.anterior = None
        self.actual = lista.prim
    
    def avanzar(self):
        self.anterior = self.actual
        self.actual = self.actual.prox

    def dato_actual(self):
        return self.actual.dato
    
    def esta_al_final(self):
        return self.actual is None
    
    def insertar(self, x):
        nuevo = _Nodo(x)
        if self.anterior:
            nuevo.prox = self.anterior.prox
            self.anterior.prox = nuevo
        else:
            nuevo.prox = self.lista.prim
            self.lista.prim = nuevo
        self.actual = nuevo

    def eliminar(self):
        dato = self.dato_actual()
        if self.anterior:
            self.anterior.prox = self.actual.prox
            self.actual = self.anterior.prox
        else:
            self.lista.prim = self.actual.prox
            self.actual = self.lista.prim
        return dato

    def __next__(self):
        if self.esta_al_final():
            raise StopIteration
        dato = self.dato_actual()
        self.avanzar()
        return dato

