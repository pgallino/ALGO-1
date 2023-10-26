"""Funcion recursiva que cuenta la cantidad de veces que aparece E y cuantas A y devuelve True si hay mas A o false si hay mas E"""


def _tiene_mas_letra_a(cadena, le, la):

    if cadena == "":
        if la > le:
            return True
        else:
            return False
    
    letra = cadena[0]
    if letra == "a":
        la += 1
    
    if letra == "e":
        le += 1
    
    return _tiene_mas_letra_a(cadena[1:], le, la)

def tiene_mas_letra_a(cadena):
    la = 0
    le = 0
    return _tiene_mas_letra_a(cadena, le, la)