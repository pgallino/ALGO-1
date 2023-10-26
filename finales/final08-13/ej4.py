class _Nodo:
    def __init__(self, dato, prox):
        self.dato = dato
        self.prox = prox

class ListaEnlazada:
    def __init__(self):
        self.prim = None

    def lshift(self, n):
        #
        # HACER: implementar
        #

        if n == 0:
            return

        actual = self.prim
        contador = 1
        primero = None

        while actual:

            if contador == n:
                final = actual
            if contador == n + 1:
                primero = actual
            
            if actual.prox == None:
                actual.prox = self.prim
                break
            
            contador += 1
            actual = actual.prox
        
        if primero == None:
            return

        self.prim = primero
        final.prox = None
    
    def rshift(self, n):

        longitud = 1
        actual = self.prim

        while actual.prox:

            longitud += 1
            actual = actual.prox
        
        if n == longitud or n == 0:
            return
        
        actual = self.prim
        contador = 1

        while actual:

            if contador == longitud:

                prox_primero_actual = actual
            
            if contador == longitud - n + 1:

                primero = actual
            
            if contador == longitud - n:

                ultimo = actual
            
            contador += 1
            actual = actual.prox
        
        prox_primero_actual.prox = self.prim
        self.prim = primero
        ultimo.prox = None

        

def pruebas():

    # creamos "a mano" la lista [3] -> [5] -> [8] -> [11]
    n3 = _Nodo(11, None)
    n2 = _Nodo(8, n3)
    n1 = _Nodo(5, n2)
    n0 = _Nodo(3, n1)
    lista = ListaEnlazada()
    lista.prim = n0

    lista.rshift(0)

    assert lista.prim.dato == 3
    assert lista.prim.prox.dato == 5
    assert lista.prim.prox.prox.dato == 8
    assert lista.prim.prox.prox.prox.dato == 11

    # OPCIONAL: Pruebas adicionales

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
