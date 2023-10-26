
class NodoABB:
    def __init__(self, dato, izq=None, der=None):
        self.dato = dato
        self.izq = izq
        self.der = der

    def buscar(self, dato):
        
        if self.dato == dato:
            return self
        
        elif self.dato > dato and self.izq == None:
            return None
        
        elif self.dato < dato and self.der == None:
            return None
        
        elif self.dato > dato:
            return self.izq.buscar(dato)
        
        elif self.dato < dato:
            return self.der.buscar(dato)

def pruebas():
    # el árbol ejemplo del enunciado
    n1 = NodoABB(1)
    n4 = NodoABB(4)
    n7 = NodoABB(7)
    n13 = NodoABB(13)
    n14 = NodoABB(14, izq = n13)
    n10 = NodoABB(10, der = n14)
    n6 = NodoABB(6, izq = n4, der = n7)
    n3 = NodoABB(3, izq = n1, der = n6)
    raiz = NodoABB(8, izq = n3, der = n10)

    nodo = raiz.buscar(6)
    assert(nodo is n6)

    # OPCIONAL: pruebas adicionales. Ejemplo: buscar un valor que no exista

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
