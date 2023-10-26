# Se tiene una implementación de  ListaEnlazada  con únicamente una referencia al primer nodo. Implementar el metodo swap_secciones(i, j) que recibe dos enteros. 
# El método va a colocar todos los elementos que estan después de la posición j antes de la posición i, 
# y todos los elementos que estaban antes de la posición i después de la posición j (intercambiando el lugar que ocupan estas secciones en la lista). 
# Notar que los elementos entre las posiciones i y j inclusive no se intercambian.
# Importante: asumir que i es siempre menor a j. Si algún indice está fuera del rango de la lista, levantar una excepción
# Ejemplo:
# >>> print(le)
# [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
# >>> le.swap_secciones(3, 8)
# >>> print(le)
# [10,11,12,13,14,4,5,6,7,8,9,1,2,3]

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
    def swap_secciones(self, i, j):
        
        actual = self.prim
        marcado1 = actual
        contador = 0
        while actual.prox:
            if contador == i-1:
                marcado2 = actual
                marcado3 = actual.prox
            elif contador == j:
                marcado4 = actual
                marcado5 = actual.prox
            actual = actual.prox
            contador += 1
        
        if contador < i or contador < j:
            raise ValueError("Se pasó de los límites")
        
        marcado6 = actual
        marcado6.prox = marcado3
        marcado4.prox = marcado1
        self.prim = marcado5
        marcado2.prox = None
        


le = ListaEnlazada()
le_res = ListaEnlazada()
le.crear_desde([1,2,3,4,5,6,7,8,9,10,11,12,13,14])
le_res.crear_desde([10,11,12,13,14,4,5,6,7,8,9,1,2,3])
le.swap_secciones(3,8)
print(le)
print(le_res)
assert le == le_res

