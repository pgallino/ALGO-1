"""Escribir una función recursiva que recibe una cadena s y un caracter c, y devuelve la cantidad de apariciones de c en s.

Nota: La solución no debe utilizar funciones como find() o rindex()"""

def _contar_apariciones(s, c, cantidad):

    if s == "":
        return cantidad
    
    if s[0] == c:
        return _contar_apariciones(s[1:], c, cantidad + 1)
    
    else:
        return _contar_apariciones(s[1:], c, cantidad)

def contar_apariciones(s,c):
    cantidad = 0
    return _contar_apariciones(s, c, cantidad)


print(contar_apariciones("perro lindo me encanta", "i"))