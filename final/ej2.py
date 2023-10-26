class Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

class ListaEnlazada:
    def __init__(self):
        self.prim = None

    def hay_ciclo(self):
        # HACER: implementar la función

        tortuga = self.prim
        liebre = self.prim

        while liebre.prox.prox:

            if liebre == tortuga and liebre != self.prim:
                return True
            
            liebre = liebre.prox.prox
            tortuga = tortuga.prox

        while tortuga.prox.prox: #verifico que si la liebre llego al final, no sea igual a la tortuga mientras llega al anteultimo. 
                                 #lo freno en el anteultimo porque en el ultimo nodo son iguales.
            if tortuga == liebre:
                return True
            
            tortuga = tortuga.prox
        
        return False

def pruebas():
    #  creamos "a mano" la lista: 10 -> 20 -> 30 -> 40
    n0 = Nodo(10)
    n1 = Nodo(20)
    n2 = Nodo(30)
    n3 = Nodo(40)
    n0.prox = n1
    n1.prox = n2
    n2.prox = n3

    L = ListaEnlazada()
    L.prim = n0

    assert(not L.hay_ciclo())

    n3.prox = n1

    assert(L.hay_ciclo())

    # OPCIONAL: Pruebas adicionales

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
