# 1. Se tiene la clase `ListaEnlazada` implementada únicamente con una referencia al
# primer nodo.  Implementar el método `slice(inicio, fin)` que devuelve una nueva
# `ListaEnlazada` incluyendo sólo los elementos ubicados entre las posiciones
# `inicio` (inclusive) y `fin` (no inclusive).  La nueva lista enlazada debe ser
# recorrida una sola vez (es decir, no se puede usar el método `append()`).

# Nota: En caso de que el valor de `inicio` sea menor a 0 toma los elementos a
# partir de la posición 0, y si el `fin` excede el largo de la lista, toma los
# elementos hasta el final de la misma.

class _Nodo:
    def __init__(self, dato, prox=None):
        self.prox = prox
        self.dato = dato

class ListaEnlazada:
    def __init__(self):
        self.prim = None
    
    # Este método **no** es parte de la lista enlazada y sólo está 
    # para simplificar las pruebas
    def crear_desde(self, lista):
      for elemento in lista:
        self.append(elemento)

    # Este método **no** es parte de la lista enlazada y sólo está 
    # para simplificar las pruebas
    def append(self, elemento):
        if not self.prim:
            self.prim = _Nodo(elemento)
            return
        
        actual = self.prim
        while actual.prox:
            actual = actual.prox
        actual.prox = _Nodo(elemento)

    # Este método **no** es parte de la lista enlazada y sólo está 
    # para simplificar las pruebas
    def __eq__(self, other):
        act = self.prim
        act_other = other.prim

        while act and act_other:
            if act.dato != act_other.dato:
                return False
            act = act.prox
            act_other = act_other.prox
        
        if not act and act_other or not act_other and act:
            return False
        
        return True

    # Este método **no** es parte de la lista enlazada y sólo está 
    # para simplificar las pruebas
    def __str__(self):
        '''
        Devuelve una representación en la forma {[elem_1] -> [elem_2] -> ... }
        de la lista enlazada.
        '''
        actual = self.prim
        
        s = '{'
        while actual:
            s += f'[{actual.dato}] -> '
            actual = actual.prox
        
        return s.rstrip(' -> ') + '}'

    # Completar el siguiente metodo
    def slice(self, inicio, fin):

        if inicio < 0:
            inicio = 0

        nueva = ListaEnlazada()
        contador = 0

        actual = self.prim
        anterior = None

        while actual.prox:

            if inicio <= contador < fin:
                nuevo_nodo = _Nodo(actual.dato)
                if anterior == None:
                    nueva.prim = nuevo_nodo
                    anterior = nueva.prim
                else:
                    anterior.prox = nuevo_nodo
                    anterior = anterior.prox
            
            actual = actual.prox
            contador += 1
        
        if contador < fin:
            nuevo_nodo = _Nodo(actual.dato)
            anterior.prox = nuevo_nodo
        
        return nueva


le = ListaEnlazada()
le_res = ListaEnlazada()
le.crear_desde([3, 4, 5, 6, 7, 8])
le_res.crear_desde([4, 5, 6])

print(le.slice(1, 6))

assert le.slice(1, 4) == le_res
assert le.slice(-1, 7) == le


