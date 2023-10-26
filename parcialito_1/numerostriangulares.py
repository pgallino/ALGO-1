"""Ejercicio 2.7. Escribir un programa que le pregunte al usuario un número n e imprima los
primeros n números triangulares, junto con su índice. Los números triangulares se obtienen
mediante la suma de los números naturales desde 1 hasta n. Es decir, si se piden los primeros 5
números triangulares, el programa debe imprimir:
1 - 1
2 - 3
3 - 6
4 - 10
5 - 15"""

def imprimirtriangulares():
    n=int(input("ingrese el número: "))
    x=0
    for i in range(1,n+1):
        indice=i
        x += indice
        print(f"{indice} - {x}")