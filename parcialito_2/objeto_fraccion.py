from math import gcd

class Fraccion():

    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise Exception("No se puede dividir por cero")
        else:
            self.num = numerador
            self.den = denominador
            self.simplificar()

    def simplificar(self):
        minimo_comun_divisor = gcd(self.num , self.den)
        self.num = self.num // minimo_comun_divisor
        self.den = self.den // minimo_comun_divisor
    
    def __str__(self):
        return f"{self.num}/{self.den}"
    
    def __add__(self, otra):
        den_suma = self.den * otra.den
        num_suma = self.num * otra.den + otra.num * self.den
        return Fraccion(num_suma, den_suma)

    def __mul__(self, otra):
        num_multi = self.num * otra.num
        den_multi = self.den * otra.den
        return Fraccion(num_multi, den_multi)

    def __eq__(self, otra):
        return self.num == otra.num and self.den == otra.den
    
    def __lt__(self, otra):

        numero1 = self.num/self.den
        numero2 = otra.num/otra.den

        if numero1 > numero2:
            return f"{self} es mas grande que {otra}"
        elif numero1 < numero2:
            return f"{self} es mas chico que {otra}"