class ListaEnlazada:

    def eliminar_consecutivos(self):
    
        if self.prim == None:
            return
        
        elif self.__len__() == 1:
            return
        
        actual = self.prim
    
        while actual.prox:
            if actual.dato == actual.prox.dato:
                actual.prox = actual.prox.prox
            else:
                actual = actual.prox

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
    
    def __str__(self):
        return str(self.dato)
    
                
l1 = ListaEnlazada()
l1.append(3)
l1.append(4)
l1.append(4)
l1.append(4)
l1.append(1)
l1.append(4)
l1.append(4)
l1.append(4)
l1.eliminar_consecutivos()