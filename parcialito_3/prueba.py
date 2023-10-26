class _Nodo:

    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)

class ListaEnlazada:

    def completar_huecos(self):
        
        actual = self.prim
        
        while actual.prox:

            if actual.dato + 1 != actual.prox.dato and actual.prox.dato > actual.dato or actual.dato - 1 != actual.prox.dato and actual.prox.dato < actual.dato:
    
                if actual.prox.dato > actual.dato:
                    nodo_nuevo = _Nodo((actual.dato) + 1)
                    nodo_nuevo.prox = actual.prox
                    actual.prox = nodo_nuevo
                    actual = actual.prox
                elif actual.prox.dato < actual.dato:
                    nodo_nuevo = _Nodo((actual.dato) - 1)
                    nodo_nuevo.prox = actual.prox
                    actual.prox = nodo_nuevo
                    actual = actual.prox
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



le = ListaEnlazada()
le_res = ListaEnlazada()
le.append(1)
le.append(4)
le.append(3)
le.append(1)
le.append(3)
print(le)
le_res.append(1)
le_res.append(2)
le_res.append(3)
le_res.append(4)
le_res.append(3)
le_res.append(2)
le_res.append(1)
le_res.append(2)
le_res.append(3)
le.completar_huecos()
print(le)
print(le_res)
assert le == le_res