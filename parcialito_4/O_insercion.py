def ord_insercion(L):
    """Ordena una lista de elementos según el método de inserción.
    Pre: los elementos de la lista deben ser comparables.
    Post: la lista está ordenada.
    """
    for i in range(1, len(L)):
        insertar_ordenado(L, i)

def insertar_ordenado(L, i):
    """Pre: L[:i] está ordenada
    Post: L[:i+1] está ordenada y contiene los mismos elementos
    que estaban en L[:i] más el elemento que estaba en i.
    """
    v = L[i]
    j = i - 1
    while j >= 0 and L[j] > v:
        L[j + 1] = L[j]
        j -= 1
    L[j + 1] = v
