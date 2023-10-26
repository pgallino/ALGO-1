valores_permitidos = {1,2,5,10,20,50,100,200,500,1000}
class Caja:

    def __init__(self, diccionario):
        for clave in diccionario:
            if not clave in valores_permitidos:
                raise ValueError(f"""Denominación "{clave}" no permitida""")
        self.dinero = diccionario

    def __str__(self):
        total = 0
        for clave in self.dinero:
            total += clave * self.dinero[clave]
        return f"Caja {self.dinero} total: {total} pesos"
    
    def agregar(self, otro):
        nueva_caja_agregar={}
        for clave in otro:
            if not clave in valores_permitidos:
                raise ValueError(f"""Denominación "{clave}" no permitida""")
            else:
                nueva_caja_agregar[clave] = self.dinero.get(clave, 0) + otro[clave]
        for clave in self.dinero:
            if not clave in otro:
                nueva_caja_agregar[clave] = self.dinero[clave]
        self.dinero = nueva_caja_agregar

    def quitar(self, caja_quitar):
        nueva_caja_quitar={}
        valor = 0
        for clave in caja_quitar:
            valor += clave * caja_quitar[clave]
            if not clave in self.dinero:
                raise Exception("No hay de esos billetes")
            elif caja_quitar[clave] > self.dinero[clave]:
                raise ValueError(f"""No hay suficientes billetes de denominación \"{clave}\"""")
            elif caja_quitar[clave] == self.dinero[clave]:
                continue
            else:
                nueva_caja_quitar[clave] = self.dinero[clave] - caja_quitar[clave]

        for clave in self.dinero:
            if not clave in caja_quitar:
                nueva_caja_quitar[clave] = self.dinero[clave]

        self.dinero = nueva_caja_quitar
        return valor
