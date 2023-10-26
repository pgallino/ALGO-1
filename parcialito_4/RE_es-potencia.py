"""Función recursiva que recibe 2 enteros n y b y devuelva True si n es potencia de b."""

def es_potencia(n, b):
    if b == n:
        return True
    
    if n < b:
        return False
    
    else:
        return es_potencia(n/b, b)

print(es_potencia(10,2))