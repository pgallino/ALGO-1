"""Implementar una clase Carta, que se crea a partir de un palo y un valor. 

Las cartas deben poder imprimirse de la forma <valor> de <palo>. 

Las cartas deben poder compararse entre ellas:

Una carta vale menos que otra si al ser del mismo palo su valor es menor, o si al ser de distintos palos el propio es menor que el palo de la otra carta

(suponer que ya está implementada una clase Palo, que implementa los métodos __eq__, __lt__ y __str__)."""

class Carta:

    def __init__(self, palo, valor):

        self.valor = valor
        self.palo = palo
    
    def __str__(self):

        return f"{self.valor} de {self.palo}"

    def __eq__(self, otra):
        
        return self.palo == otra.palo and self.valor == otra.valor

    def __lt__(self, otra):

        if self.valor < otra.valor and self.palo == otra.palo:
            return f"{self} es menor que {otra}"
        elif self.valor > otra.valor and self.palo == otra.palo:
            return f"{self} es mayor que {otra}"
        elif self.palo > otra.palo:
            return f"{self} es mayor que {otra}"
        elif self.palo < otra.palo:
            return f"{self} es menor que {otra}"


