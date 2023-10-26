"""Escribir una función recursiva que calcule recursivamente el n-ésimo número triangular (el número 1 + 2 + 3 + … + n)."""

def numero_triangular(n):

    if n == 1:
        return n
    
    return numero_triangular(n - 1) + n

"""explicación: llega hasta 1 y devuelve 1, entonces el siguiente es 1 + n (n sería 2), el siguiente es 3 + n (n sería 3), el siguiente es 6 + n (n sería 4) ..."""