"""Ejercicio 138 pilas

Se tiene una Cola con los números del 1 al 5 encolados en orden de menor a mayor. 

Se cuenta además con una clase que posee dos pilas y tres métodos: paso1(cola), paso2(), paso3().

paso1(cola): desencola de la Cola y apila el numero obtenido en la primera de las pilas de la clase
paso2(): desapila el tope de la primer pila y lo apila en la segunda
paso3(): desapila el tope de la segunda pila y lo imprime

Determinar cuales de las siguientes opciones de impresión por pantalla son posibles de ocurrir y cuáles no. 

Justficiar, en caso de que sea posible, con el orden de las llamadas a los pasos:

primero  ultimo
   |       |
   v       v
a. 4 5 3 1 2
b. 2 3 1 5 4"""

from Pila import Pila
from Cola import Cola

class Operaciones:

    def __init__(self):
        self.pila1 = Pila()
        self.pila2 = Pila()

    def paso1(self, cola):
        self.pila1.apilar(cola.desencolar())

    def paso2(self):
        self.pila2.apilar(self.pila1.desapilar())
    
    def paso3(self):
        print(self.pila2.desapilar())

op = Operaciones()
cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
cola.encolar(4)
cola.encolar(5)

op.paso1(cola)
op.paso1(cola)
op.paso1(cola)
op.paso2()
op.paso2()
op.paso3()
op.paso3()
op.paso2()
op.paso3()
op.paso1(cola)
op.paso1(cola)
op.paso2()
op.paso3()
op.paso2()
op.paso3()

print("fin caso 1")

op = Operaciones()
cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
cola.encolar(4)
cola.encolar(5)

op.paso1(cola)
op.paso1(cola)
op.paso1(cola)
op.paso1(cola)
op.paso1(cola)
op.paso2()
op.paso2()
op.paso3()
op.paso3()

op.paso2()
op.paso3()

op.paso2()
op.paso2()
op.paso3()
op.paso3()




    
