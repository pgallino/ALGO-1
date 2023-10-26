def _posiciones_de(a, b, contador, lista):
    
    if a == "":
        return lista
    
    if b == a[:len(b)]:
        lista.append(contador)
        return _posiciones_de(a[1:],b, contador + 1, lista)
    
    else:
        return _posiciones_de(a[1:],b, contador + 1, lista)
    
def posiciones_de(a, b):
    lista = []
    contador = 0
    return _posiciones_de(a, b, contador, lista)