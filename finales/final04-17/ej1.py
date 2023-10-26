class Nodo:
    def __init__(self, dato, izq=None, der=None):
        self.dato = dato
        self.izq = izq
        self.der = der

    def recorrer(self, camino):

        if camino and camino[0] != "0" and camino[0] != "1":
            return None
        
        elif (self.izq == None and self.der == None) and camino != "":
            return None
        
        else:

            if camino == "":
                return self.dato
            
            elif int(camino[0]) == 0:
                return self.izq.recorrer(camino[1:])
            
            elif int(camino[0]) == 1:
                return self.der.recorrer(camino[1:])

def pruebas():
    # el árbol ejemplo del enunciado
    raiz = Nodo(2,
        izq = Nodo(7,
            izq = Nodo(2),
            der = Nodo(6,
                izq = Nodo(5),
                der = Nodo(11),
            ),
        ),
        der = Nodo(5,
            der = Nodo(9,
                izq = Nodo(4),
            ),
        ),
    )

    assert raiz.recorrer("110011101010") == None
    assert raiz.recorrer("abdw") == None
    assert raiz.recorrer("") == 2
    assert raiz.recorrer("010") == 5

    # OPCIONAL: pruebas adicionales

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
