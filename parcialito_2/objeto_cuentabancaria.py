class Cuenta:
    
    def __init__(self, propietario):
        self.propietario = propietario
        self.deposito = 0
        self.mov = []

    def __str__(self):
        return f"Cuenta de {self.propietario}"

    def acreditar(self, monto, tipo):
        self.deposito += monto
        self.mov.append(("acreditación", monto, tipo))

    def extraer(self, monto, tipo):
        if self.deposito < monto:
            raise ValueError("Fondos Insuficientes")
        else:
            self.deposito -= monto
            self.mov.append(("extracción", monto, tipo))

    def transferir(self, monto, otra):
        if self.deposito < monto:
            raise ValueError("Fondos Insuficientes")
        else:
            self.deposito -= monto
            self.mov.append(("extracción", monto, str(otra)))
            otra.deposito += monto
            otra.mov.append(("acreditación", monto, str(self)))
    def saldo(self):
        return self.deposito
    
    def movimientos(self):
        return self.mov