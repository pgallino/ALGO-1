class RegistroDeDesplazamiento:
    
    def __init__(self, n):
        self.bits = "0" * n
    
    def rshift(self, bit):
        valor = self.bits[-1]
        self.bits = str(bit) + self.bits[:-1]
        return int(valor)
    
    def lshift(self, bit):
        valor = self.bits[0]
        self.bits = self.bits[1:] + str(bit)
        return int(valor)
    
    def __str__(self):
        return self.bits

def pruebas():
    r = RegistroDeDesplazamiento(4)

    assert str(r) == '0000'
    assert r.rshift(0) == 0
    assert str(r) == '0000'
    assert r.rshift(1) == 0
    assert str(r) == '1000'
    assert r.rshift(0) == 0
    assert str(r) == '0100'
    assert r.rshift(0) == 0
    assert str(r) == '0010'
    assert r.rshift(0) == 0
    assert str(r) == '0001'
    assert r.rshift(0) == 1
    assert str(r) == '0000'
    assert r.rshift(0) == 0
    assert str(r) == '0000'

    # OPCIONAL: pruebas adicionales (ej: probar lshift)

    assert r.lshift(1) == 0
    assert str(r) == "0001"


    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
