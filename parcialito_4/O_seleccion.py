def ord_seleccion(L):
    """Ordena una lista de elementos según el método de selección.
    Pre: los elementos de la lista deben ser comparables.
    Post: la lista está ordenada.
    """
    for i in range(len(L) - 1):
        p = buscar_elemento_minimo(L, i)
        L[p], L[i] = L[i], L[p]

def buscar_elemento_minimo(L, i):
    min = L[i]
    min_p = i
    for j in range(i + 1, len(L)):
        if L[j] < min:
            min = L[j]
            min_p = j
    return min_p

lista = [1,5,2,7,8,3,4]
ord_seleccion(lista)
print(lista)