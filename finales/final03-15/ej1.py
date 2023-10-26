
class _Nodo:
    def __init__(self, dato, prox):
        self.dato = dato
        self.prox = prox

class ListaEnlazada:
    def __init__(self):
        self.prim = None

    def esta_ordenada(self):
        #
        # HACER: implementar EN FORMA RECURSIVA (posiblemente con un wrapper)
        #
        actual = self.prim
        return self._esta_ordenada(actual)
    
    def _esta_ordenada(self, actual):

        if not actual.prox:
            return True

        elif actual.dato > actual.prox.dato:
            return False
        
        actual = actual.prox

        return self._esta_ordenada(actual)

def pruebas():

    # creamos "a mano" la lista [3] -> [5] -> [8] -> [11]
    n3 = _Nodo(11, None)
    n2 = _Nodo(8, n3)
    n1 = _Nodo(5, n2)
    n0 = _Nodo(3, n1)
    lista = ListaEnlazada()
    lista.prim = n0

    assert lista.esta_ordenada()

    # OPCIONAL: Pruebas adicionales. Sugerencias:
    # - Repetir la prueba con una lista desordenada, y verificar que la
    #   función devuelve False
    # - Repetir la prueba con una lista vacía (es indistinto lo que devuelve
    #   la funcion, pero no debería fallar)


    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
