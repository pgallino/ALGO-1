"""Implementar la clase Botella que cumpla con el siguiente comportamiento:

>> botella = Botella(500)      >> botella.cargar(300)
>> print(botella)              Exception(“La botella no cuenta con capacidad suficiente”)
Botella: 0/500cc               >> botella.servir(200)
>> botella.esta_vacia()        >> print(botella)
True                           Botella: 100/500cc
>> botella.cargar(300)         >> botella.servir(200)
>> print(botella)              Exception(“La botella no cuenta con carga suficiente”)
Botella: 300/500cc"""

class Botella:

    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.relleno = 0
    
    def __str__(self):
        return f"Botella: {self.relleno}/{self.capacidad}cc"
    
    def esta_vacia(self):
        if self.relleno == 0:
            return True
        else:
            return False
    def cargar(self, cantidad):
        if self.relleno + cantidad > self.capacidad:
            raise Exception("La botella no cuenta con capacidad suficiente")
        else:
            self.relleno = self.relleno + cantidad

    def servir(self, cantidad):
        if self.relleno - cantidad < 0:
            raise Exception("La botella no cuenta con carga suficiente")
        else:
            self.relleno = self.relleno - cantidad