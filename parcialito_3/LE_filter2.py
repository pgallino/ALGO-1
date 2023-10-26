"""Ejercicio 119 lista-enlazada
Teniendo una ListaEnlazada implementada como solo una referencia al primer nodo,

se pide implementar el método filter, que dada una función f que recibe un elemento y devuelve True o False,

remueva todos los elementos de la lista para los cuales la función devuelve False. 

(Aclaracion: el método modifica la lista, no devuelve una nueva ni tampoco utiliza estructuras axuliar, y la funcion f se recibe por parametro)"""

class _Nodo:

    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)

class ListaEnlazada:

    def filter(self, f):

        actual = self.prim

        while actual.prox:

            if f(self.prim.dato) == False:
                self.prim = actual.prox
                actual = actual.prox
                self.cant -= 1

            else:   
                if f(actual.prox.dato) == False:
                    actual.prox = actual.prox.prox
                    self.cant -= 1

                else:
                    actual = actual.prox

        if f(actual.dato) == False:
            actual = None

        

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

def es_par(n):
    return n%2 == 0

le = ListaEnlazada()
le.append(2)
le.append(4)
le.append(5)
le.append(1)
le.append(4)
le.append(3)
le.append(12)
print(le)
print(le.cant)
le.filter(es_par)
print(le)
print(le.cant)