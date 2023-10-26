"""Implementar metodo de lista enlazada de la invierta, siendo este metodo recursivo"""



class ListaEnlazada:

    def invertir_pro(self):          #version buena de invertir

        if not self.prim.prox:
            return 
            
        anterior= self.prim
        act= self.prim.prox
        self.prim= self.prim.prox
        
        self.invertir_pro()
        act.prox= anterior
        anterior.prox=None

    def invertir(self):               #version mia xd
        if self.cant == 1:
            return
        actual = self.prim
        self._invertir(actual)
    
    def _invertir(self, actual):

        if actual.prox == None:
            self.prim = None
            return actual.dato
        
        else:
            nodo = _Nodo(actual.dato)
            actual = actual.prox
        
        primero = self._invertir(actual)

        if self.prim == None:
            nuevo = _Nodo(primero)
            self.prim = nuevo
            
            nuevo.prox = nodo
        
        else:
            actual = self.prim
            while actual.prox:
                actual = actual.prox
        
            actual.prox = nodo

    def __str__(self):
        lista = "["
        actual = self.prim
        while actual:
            lista += f"{actual.dato}, "
            actual = actual.prox
        lista = lista.rstrip(", ") + "]"
        return lista
        
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


l = ListaEnlazada()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
print(l)
l.invertir()
print(l)
