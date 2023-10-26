# Se quiere modelar un perchero para colgar ropa. Se pide crear las clases `Perchero` y `Prenda` tal que se se puedan ejecutar 
# las siguientes líneas de código y se obtengan los resultados especificados:
# >>> p = Perchero(3)
# >>> p.colgar(Prenda('camisa', 1))
# >>> p.colgar(Prenda('pantalon', 1))
# >>> pantalon = p.sacar('pantalon')
# >>> print(pantalon)
# Pantalon: 1
# >>> p.sacar('remera')
# ValueError: No se encontró la prenda
# >>> p.espacio_disponible()
# 2
# >>> p.colgar(Prenda('campera', 3))
# ValueError: No hay espacio para colgar la prenda
# El constructor de `Perchero` recibe la cantidad de espacio total disponible, y el de `Prenda` recibe el nombre de la prenda y cuánto espacio ocupa

# Escribir el codigo debajo de esta linea
class Prenda:

    def __init__(self, nombre, volumen):
        self.nombre = nombre
        self.volumen = volumen
    
    def __str__(self):

        return f"{self.nombre}: {self.volumen}"
    
    def obtener_volumen(self):

        return self.volumen
    
    def obtener_nombre(self):
        
        return self.nombre

class Perchero:

    def __init__(self, espacio):

        self.espacio = espacio
        self.cantidad = 0
        self.prendas = {}    #es un diccionario con los nombres de las prendas como claves y los objetos asociados como valores
    
    def colgar(self,prenda):

        volumen = prenda.obtener_volumen()

        nombre = prenda.obtener_nombre()

        if volumen <= (self.espacio - self.cantidad):
            self.cantidad += volumen
            self.prendas[nombre] = prenda
        
        else:
            raise ValueError("No hay espacio para colgar la prenda")
    
    def sacar(self,prenda):

        nombre = prenda

        if nombre in self.prendas:

            prenda_objeto = self.prendas[nombre]

            del self.prendas[nombre]

            self.cantidad -= prenda_objeto.obtener_volumen()

            return prenda_objeto
            
        else:
            raise ValueError("No se encontró la prenda")
    
    def espacio_disponible(self):
        return self.espacio - self.cantidad



#Pruebas
p = Perchero(3)
p.colgar(Prenda('camisa', 1))
p.colgar(Prenda('pantalon', 1))
pantalon = p.sacar('pantalon')
assert(str(pantalon) == 'pantalon: 1')
hay_excepcion = True
try:
    p.sacar('remera')
    hay_excepcion = False
except ValueError:
    pass
assert hay_excepcion, "una excepcion no fue lanzada"
assert(p.espacio_disponible() == 2)
hay_excepcion = True
try:
    p.colgar(Prenda('campera', 3))
    hay_excepcion = False
except ValueError:
    pass
assert hay_excepcion, "una excepcion no fue lanzada"
