class ListaEnlazada:


    def rotar(self, N):

        if N == self.cant:
            return

        elif not self.prim:
            return


        else:

            ultimo = self.prim
            while ultimo.prox:
                ultimo = ultimo.prox

            if N > self.cant:
                N = N % self.cant
        
            nuevo_primero = self.prim
            for i in range(N):
                nuevo_primero = nuevo_primero.prox

            actual = self.prim
            while actual != nuevo_primero:
                nodo_nuevo = _Nodo(actual.dato)
                ultimo.prox = nodo_nuevo
                ultimo = nodo_nuevo
                actual = actual.prox
            
            self.prim = nuevo_primero
        
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

    def __str__(self):
        lista = "["
        actual = self.prim
        while actual:
            lista += f"{actual.dato}, "
            actual = actual.prox
        lista = lista.rstrip(", ") + "]"
        return lista

class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox
    def __str__(self):
        return str(self.dato)

le = ListaEnlazada()
le.append(1)
le.append(2)
le.append(3)
le.append(4)
le.append(5)
le.append(6)
le.append(7)
le.append(8)
print(le)
le.rotar(2)
print(f"rotada 2 pos: {le}")
le.rotar(11)
print(f"rotada 2 + 11 pos: {le}")
le.rotar(10)
print(f"rotada 2 + 11 + 10 pos: {le}")