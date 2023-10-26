"""
El triángulo de Pascal es un arreglo triangular de números que se define de la siguiente manera: Las filas se enumeran desde n = 0, de arriba hacia abajo. Los valores de cada fila se enumeran desde k = 0 (de izquierda a derecha). Los valores que se encuentran en los bordes del triángulo son 1. Cualquier otro valor se calcula sumando los dos valores contiguos
de la fila de arriba.

n = 0                  1
n = 1                1   1 
n = 2              1   2   1 
n = 3            1   3   3   1 
n = 4          1   4   6   4   1 
n = 5        1   5  10  10   5   1 
n = 6      1   6  15  20  15   6   1 
Escribir la función recursiva pascal(n, k) que calcula el valor que se encuentra en la fila n y la columna k."""

def pascal(n, k):
    
    if n == 0:
        return 1
    
    if k == n or k == 0:
        return 1
        
    return pascal(n-1, k-1) + pascal(n-1, k)

def mostrar_triangulo_pascal(alto):
    for n in range(alto + 1):
        print(' ' * (2 * (alto - n)), end='')
        for k in range(n + 1):
            print(f'{pascal(n, k) : 4}', end=' ')
        print()


mostrar_triangulo_pascal(7)