"""Ejercicio 136 pilas

Se realizan sobre una pila, una secuencia de operaciones de apilar() y desapilar().

Las operaciones de apilar() apilarán, de a uno, los números del 0 al 9 en orden (el primer apilar() apilará el 0, el segundo apilar() el 1, 

y así hasta que el décimo apilar() apile el 9). 

Cada operación de desapilar(), además de desapilar el elemento, lo imprimirá por pantalla. 

Determinar cuáles de las siguientes opciones no es posible que ocurra. 

Para cada una de las que sí son posibles, dar una secuencia de llamadas a apilar() y desapilar() que la cumpla.

a. 4 3 2 1 0 9 8 7 6 5 b. 4 6 8 7 5 3 2 9 0 1 c. 2 5 6 7 4 8 9 3 1 0 d. 4 3 2 1 0 5 6 7 8 9"""


from Pila import Pila

pila_a = Pila()
pila_a.apilar(0)
pila_a.apilar(1)
pila_a.apilar(2)
pila_a.apilar(3)
pila_a.apilar(4)
print(pila_a.desapilar())
print(pila_a.desapilar())
print(pila_a.desapilar())
print(pila_a.desapilar())
print(pila_a.desapilar())
pila_a.apilar(5)
pila_a.apilar(6)
pila_a.apilar(7)
pila_a.apilar(8)
pila_a.apilar(9)
print(pila_a.desapilar())
print(pila_a.desapilar())
print(pila_a.desapilar())
print(pila_a.desapilar())
print(pila_a.desapilar()) 

print("pila_a es posible")  #La a es posible

pila_b = Pila()
pila_b = Pila()
pila_b.apilar(0)
pila_b.apilar(1)
pila_b.apilar(2)
pila_b.apilar(3)
pila_b.apilar(4)
print(pila_b.desapilar())
print(pila_b.desapilar())
print(pila_b.desapilar())
print(pila_b.desapilar())
print(pila_b.desapilar())
pila_b.apilar(5)
print(pila_b.desapilar())
pila_b.apilar(6)
print(pila_b.desapilar())
pila_b.apilar(7)
print(pila_b.desapilar())
pila_b.apilar(8)
print(pila_b.desapilar())
pila_b.apilar(9)
print(pila_b.desapilar())

print("pila_b es posible") #La B es posible