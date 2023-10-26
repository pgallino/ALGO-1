# El algoritmo de Euclides se utiliza para calcular el máximo común divisor entre dos números. El mismo consiste en lo siguiente:
# - Dados dos números enteros, a y b, se divide el número mayor (a) por el menor (b) y se obtiene el resto de la división entera (r).
# - En caso de que el resto (r) de la división sea cero, el divisor (b) es el m.c.d.
# - En otro caso, se vuelve al primer paso, dividiendo al divisor (b) por el resto (r).
# Escribir en Python una función recursiva que devuelva el máximo común divisor entre dos numeros mediante el algoritmo de Euclides.

# Escribir el codigo debajo de esta linea
def mcd_euclides(n1, n2):
    if n1>n2:
        r = n1%n2
        if r == 0:
            return n2
        else:
            return mcd_euclides(n2, r)
    elif n2>n1:
        r = n2%n1
        if r == 0:
            return n1
        else:
            return mcd_euclides(n1, r)

# Pruebas
assert mcd_euclides(18, 24) == 6
assert mcd_euclides(150, 10) == 10