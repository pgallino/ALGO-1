class Cola:
    #
    # HACER: implementar los métodos
    #

    def __init__(self, k):
        lista = []
        for i in range(k-1):
            lista.append(None)
        
        self.lista = lista

    def encolar(self, dato):
        'lanza ColaLlenaError si no hay más lugar'
        
        contador = 0
        for i in range(len(self.lista)):
            if self.lista[i] == None:
                contador += 1
        
        if contador == 0:
            raise ColaLlenaError
        
        self.lista = [dato] + self.lista[:-1]


    def desencolar(self):
        'lanza ColaVaciaError si la cola está vacía'
        contador = 0
        for i in range(len(self.lista)):
            if self.lista[i] == None:
                contador += 1
        
        if contador == len(self.lista):
            raise ColaVaciaError
        
        dato = self.lista[-1]

        if dato == None:

            while dato == None:
                self.lista = [None] + self.lista[:-1]
                dato = self.lista[-1]
        
        self.lista = [None] + self.lista[:-1]
        return dato

class ColaVaciaError(Exception):
    pass

class ColaLlenaError(Exception):
    pass

def pruebas():
    # creamos una cola con capacidad K = 5
    c = Cola(5)

    for i in range(10):
        # la cola está vacía, desencolar() debe lanzar ColaVaciaError
        ok = False
        try:
            c.desencolar()
        except ColaVaciaError:
            ok = True
        assert ok

        # encolamos 4 elementos
        for i in range(4):
            c.encolar(i)

        # la cola está llena, encolar() debe lanzar ColaLlenaError
        ok = False
        try:
            c.encolar(5)
        except ColaLlenaError:
            ok = True
        assert ok

        # desencolamos los 4 elementos
        for i in range(4):
            assert c.desencolar() == i

        # la cola está vacía, desencolar() debe lanzar ColaVaciaError
        ok = False
        try:
            c.desencolar()
        except ColaVaciaError:
            ok = True
        assert ok

        # encolamos y desencolamos para desplazar el inicio
        c.encolar(1)
        assert c.desencolar() == 1


    # OPCIONAL: agregar más casos de prueba.

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
