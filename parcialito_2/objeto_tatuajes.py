"""Se tiene implementada la clase Tatuaje(nombre,area,dolor) cuya área y dolor son enteros mayores a 0.

Implementar las clases Tatuador(nombre) y Brazo(area, aguante), que se comporten de la siguiente forma:

>>> tatuaje_dragon = Tatuaje("Dragón",10,30)    >>> tatuador.tatuar(brazo2, tatuaje_panda)
>>> tatuaje_panda = Tatuaje("Panda",10,10)      ValueError: Ya no te queda más lugar
>>> brazo1 = Brazo(20, 10)                      >>> tatuador.tatuar(brazo1, tatuaje_panda)
>>> brazo2 = Brazo(10, 100)                     >>> tatuador.tatuar(brazo1, tatuaje_panda)
>>> tatuador = Tatuador("Miguel")               >>> tatuador.tatuar(brazo1, tatuaje_panda)
>>> tatuador.tatuar(brazo1, tatuaje_dragon)     ValueError: Ya no te queda más lugar
ValueError: No te lo vas a bancar               >>> print(tatuador)
>>> tatuador.tatuar(brazo2, tatuaje_dragon)     Miguel: 3 tatuajes realizados"""

class Tatuaje:

    def __init__(self, dibujo, area, dolor):

        self.dibujo = dibujo
        self.area = area
        self.dolor = dolor

class Brazo:

    def __init__(self, area, aguante):

        self.area = area
        self.aguante = aguante

    def aguanta_dolor(self, dolor):
        if dolor > self.aguante:
            return False
        elif dolor <= self.aguante: 
            return True
    
    def entra_tatuaje(self, area):
        if area > self.area:
            return False
        elif area <= self.area:
            return True
    
    def ocupar_area(self, area, dolor):
        if self.entra_tatuaje(area) == True and self.aguanta_dolor(dolor) == True:
            self.area = self.area - area
        elif self.entra_tatuaje(area) == False:
            raise ValueError("No te queda mas lugar")
        elif self.aguanta_dolor(dolor) == False:
            raise ValueError("No te la vas a bancar")

class Tatuador:

    def __init__(self, nombre):
        
        self.nombre = nombre
        self.tatuajes = 0
    
    def tatuar(self, brazo, tatuaje):
        brazo.ocupar_area(tatuaje.area, tatuaje.dolor)
        self.tatuajes +=1
    
    def __str__(self):
        if self.tatuajes > 1:
            return f"{self.nombre}: {self.tatuajes} tatuajes realizados"
        elif self.tatuajes == 1:
            return f"{self.nombre}: {self.tatuajes} tatuaje realizado"
        elif self.tatuajes == 0:
            return f"{self.nombre}: no hizo ningún tatuaje"

