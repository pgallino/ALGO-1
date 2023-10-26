
"""Escribir un programa que pida dos números enteros al usuario (a y b) e imprima los primeros a múltiplos de b.

El programa debe validar que cada número que ingrese el usuario sea un entero positivo y, en caso de que no lo sea, 

solicitarlo nuevamente (hasta que se ingrese algo correcto).

Ejemplo:

Ingrese el número 'a': 4
Ingrese el número 'b': 6
6
12
18
24"""

def multiplos():

    a = "-1"
    b = "-1"

    while (a.isdigit() == False) or int(a) < 1:
        a = input("Ingrese el número 'a': ")
    
    while (b.isdigit() == False) or int(b) < 1:
        b = input("Ingrese el número 'b': ")
    
    a = int(a)
    b = int(b)
    
    for i in range(1, a+1):
        print(i * b)

multiplos()