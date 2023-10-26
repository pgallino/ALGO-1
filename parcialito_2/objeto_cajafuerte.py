class CajaFuerte:

    def __init__(self, clave):
        self.clave = clave
        self.abierta = False
        self.objeto = 0
    def abrir(self, clave):
        if clave == self.clave:
            self.abierta = True
        elif clave != self.clave:
            raise Exception("La clave es inválida")
    def cerrar(self):
        self.abierta = False

    def esta_abierta(self):
        if self.abierta == False:
            return False
        else:
            return True
    def guardar(self, objeto):
        if self.abierta == False:
            raise Exception("La caja fuerte está cerrada")
        elif self.objeto != 0:
            raise Exception("No se puede guardar más de una cosa")
        else:
            self.objeto = objeto

    
    def sacar(self):
        if self.abierta == False:
            raise Exception("La caja fuerte está cerrada")
        elif self.objeto == 0:
            raise Exception("No hay nada para sacar")
        else:
            sacado = self.objeto
            self.objeto = 0
            return sacado